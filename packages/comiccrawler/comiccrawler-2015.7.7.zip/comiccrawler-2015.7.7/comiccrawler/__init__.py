#! python3

"""Comic Crawler

Usage:
  comiccrawler domains
  comiccrawler download URL [--dest SAVE_FOLDER]
  comiccrawler gui
  comiccrawler migrate
  comiccrawler (--help | --version)

Commands:
  domains             List supported domains.
  download URL        Download from the URL.
  gui                 Launch TKinter GUI.
  migrate             Migrate from old version, convert save file to new
                      format.

Options:
  --dest SAVE_FOLDER  Set download save path. [default: .]
  --help              Show help message.
  --version           Show current version.

Sub modules:
  comiccrawler.core   Core functions of downloading, analyzing.
  comiccrawler.error  Errors.
  comiccrawler.mods   Import download modules.
"""

__version__ = "2015.7.7"

import subprocess, traceback, json

from worker import Worker, UserWorker, WorkerExit
from os import path
from collections import OrderedDict

from .safeprint import safeprint
from .config import setting, section
from .core import Mission, Episode, download, analyze, safefilepath
from .io import content_read, content_write, is_file
from .mods import list_domain, load_config

from . import config, io

def shallow(dict, exclude=None):
	"""Return a shallow copy of a dict.

	Arguments:
	exclude - A list of key name which should not to copy. (default: None)
	"""
	new_dict = {}
	for key in dict:
		if not exclude or key not in exclude:
			new_dict[key] = dict[key]
	return new_dict

class MissionPoolEncoder(json.JSONEncoder):
	"""Encode Mission, Episode to json."""

	def default(self, object):
		if isinstance(object, Mission):
			return shallow(vars(object), exclude=["module", "thread"])

		if isinstance(object, Episode):
			return shallow(vars(object))

		return super().default(object)

class MissionManager(UserWorker):
	"""Save, load missions from files"""

	def __init__(self):
		"""Construct."""
		super().__init__()

		self.pool = {}
		self.view = OrderedDict()
		self.library = OrderedDict()
		self.edit = False

	def worker(self):
		"""Override. The worker target."""
		@self.listen("MISSION_PROPERTY_CHANGED")
		@self.listen("DOWNLOAD_EP_COMPLETE")
		def dummy():
			"""Set the edit flag after mission changed."""
			self.edit = True

		@self.listen("WORKER_DONE")
		def dummy():
			"""Save missions after the thread terminate."""
			self.save()

		self.load()
		while True:
			self.wait(setting.getint("autosave", 5))
			if self.edit:
				self.save()

	def save(self):
		"""Save missions to json."""
		content_write(
			"~/comiccrawler/pool.json",
			json.dumps(
				list(self.pool.values()),
				cls=MissionPoolEncoder,
				indent=4,
				ensure_ascii=False
			)
		)
		content_write(
			"~/comiccrawler/view.json",
			json.dumps(
				list(self.view),
				indent=4,
				ensure_ascii=False
			)
		)
		content_write(
			"~/comiccrawler/library.json",
			json.dumps(
				list(self.library),
				indent=4,
				ensure_ascii=False
			)
		)
		self.edit = False

	def load(self):
		"""Load mission from json.

		If it fail to load missions, create json backup in
		`~/comiccrawler/invalid-save`.
		"""
		try:
			self._load()
		except Exception:
			import time
			dest = path.join(
				"~/comiccrawler/invalid-save",
				time.strftime("%Y-%m-%d %H.%M.%S")
			)

			exc = traceback.format_exc()

			safeprint("Can't read save files! Move files to {}\n\n{}".format(
				dest,
				exc
			))

			io.move(
				"~/comiccrawler/*.json",
				dest
			)

			self.bubble("MISSION_POOL_LOAD_FAILED", (dest, exc))

	def _load(self):
		"""Load missions from json. Called by MissionManager.load."""
		pool = []
		view = []
		library = []

		if is_file("~/comiccrawler/pool.json"):
			pool = json.loads(content_read("~/comiccrawler/pool.json"))

		if is_file("~/comiccrawler/view.json"):
			view = json.loads(content_read("~/comiccrawler/view.json"))

		if is_file("~/comiccrawler/library.json"):
			library = json.loads(content_read("~/comiccrawler/library.json"))

		for m_data in pool:
			# reset state
			if m_data["state"] in ("DOWNLOADING", "ANALYZING"):
				m_data["state"] = "ERROR"
			# build episodes
			episodes = []
			for ep_data in m_data["episodes"]:
				episodes.append(Episode(**ep_data))
			m_data["episodes"] = episodes
			mission = Mission(**m_data)
			self._add(mission)

		self.add("view", *[self.pool[url] for url in view])
		self.add("library", *[self.pool[url] for url in library])

	def _add(self, mission):
		"""Add mission to public pool."""
		if mission.url not in self.pool:
			self.add_child(mission)
			self.pool[mission.url] = mission

	def add(self, pool_name, *missions):
		"""Add missions to pool."""
		pool = getattr(self, pool_name)

		for mission in missions:
			self._add(mission)
			pool[mission.url] = mission

		self.bubble("MISSION_LIST_REARRANGED", pool)
		self.edit = True

	def remove(self, pool_name, *missions):
		"""Remove missions from pool."""
		pool = getattr(self, pool_name)

		# check mission state
		missions = [m for m in missions if m.state not in ("ANALYZING", "DOWNLOADING")]

		for mission in missions:
			del pool[mission.url]
			if mission.url not in self.view and mission.url not in self.library:
				del self.pool[mission.url]

		self.bubble("MISSION_LIST_REARRANGED", pool)
		self.edit = True

	def lift(self, pool_name, *missions):
		"""Lift missions to the top."""
		pool = getattr(self, pool_name)
		for mission in reversed(missions):
			pool.move_to_end(mission.url, last=False)
		self.bubble("MISSION_LIST_REARRANGED", pool)
		self.edit = True

	def drop(self, pool_name, *missions):
		"""Drop missions to the bottom."""
		pool = getattr(self, pool_name)
		for mission in missions:
			pool.move_to_end(mission.url)
		self.bubble("MISSION_LIST_REARRANGED", pool)
		self.edit = True

	def get_by_state(self, pool_name, states, all=False):
		"""Get missions by states."""
		if not all:
			for mission in getattr(self, pool_name).values():
				if mission.state in states:
					return mission
			return None
		else:
			output = []
			for mission in getattr(self, pool_name).values():
				if mission.state in states:
					output.append(mission)
			return output

	def get_by_url(self, url, pool_name=None):
		"""Get mission by url."""
		if not pool_name:
			return self.pool[url]
		return getattr(self, pool_name)[url]

class DownloadManager(UserWorker):
	"""Create a download manager used in GUI."""

	def __init__(self):
		"""Construct."""
		super().__init__()

		self.mission_manager = self.create_child(MissionManager)

		self.download_thread = None
		self.analyze_threads = set()
		self.library_thread = None

	def worker(self):
		"""Override."""
		@self.listen("DOWNLOAD_ERROR")
		def dummy(mission):
			self.mission_manager.drop("view", mission)

		@self.listen("DOWNLOAD_FINISHED")
		def dummy(mission, thread):
			"""After download, execute command."""
			if thread is not self.download_thread:
				return

			command = (
				setting.get("runafterdownload"),
				path.join(
					setting["savepath"],
					safefilepath(mission.title)
				)
			)

			if not command[0]:
				return

			try:
				subprocess.call(command)
			except Exception as er:
				safeprint("Failed to run process: {}\n{}".format(command, traceback.format_exc()))

		@self.listen("DOWNLOAD_FINISHED")
		@self.listen("DOWNLOAD_ERROR")
		def dummy(mission, thread):
			"""After download, continue next mission"""
			if thread is self.download_thread:
				mission = self.get_mission_to_download()
				if mission:
					worker = self.create_child(download)
					worker.start(mission, setting["savepath"])
					self.download_thread = worker
				else:
					safeprint("All download completed")

		@self.listen("ANALYZE_FAILED")
		@self.listen("ANALYZE_FINISHED")
		def dummy(mission, thread):
			"""After analyze, continue next (library)"""
			if thread is self.library_thread:
				if mission.state == "UPDATE":
					self.mission_manager.lift("library", mission)

				mission = self.get_mission_to_check_update()
				if mission:
					self.library_thread = self.create_child(analyze).start(mission)

		@self.listen("ANALYZE_FINISHED")
		def dummy(mission, thread):
			if thread in self.analyze_threads:
				self.analyze_threads.remove(thread)
				self.bubble("AFTER_ANALYZE", mission)

		@self.listen("ANALYZE_FAILED")
		def dummy(mission, thread):
			if thread in self.analyze_threads:
				self.analyze_threads.remove(thread)
				self.bubble("AFTER_ANALYZE_FAILED", mission)

		self.reload_config()
		self.mission_manager.start()

		if setting.getboolean("libraryautocheck"):
			self.start_check_update()

		self.message_loop()

	def get_mission_to_download(self):
		"""Select those missions which available to download."""
		states = ("ANALYZED", "PAUSE", "ERROR")
		return self.mission_manager.get_by_state("view", states)

	def get_mission_to_check_update(self):
		"""Select those missions which available to check update."""
		states = ("ANALYZE_INIT",)
		return self.mission_manager.get_by_state("library", states)

	def reload_config(self):
		"""Load config from setting.ini and call mods.load_config."""
		config.load("~/comiccrawler/setting.ini")

		default = {
			"savepath": "~/comiccrawler/download",
			"runafterdownload": "",
			"libraryautocheck": "True"
		}

		section("DEFAULT", default)

		setting["savepath"] = path.normpath(setting["savepath"])

		load_config()

	def create_mission(self, url):
		"""Create the mission from url."""
		return Mission(url=url)

	def start_analyze(self, mission):
		"""Analyze the mission."""
		thread = self.create_child(analyze)
		self.analyze_threads.add(thread)
		thread.start(mission)

	def start_download(self):
		"""Start downloading."""
		if self.download_thread and self.download_thread.is_running():
			return

		mission = self.get_mission_to_download()
		if not mission:
			safeprint("所有任務已下載完成")
			return

		safeprint("Start download " + mission.title)
		self.download_thread = self.create_child(download).start(mission, setting["savepath"])

	def stop_download(self):
		"""Stop downloading."""
		if self.download_thread:
			self.download_thread.stop()
			safeprint("Stop downloading")

	def start_check_update(self):
		"""Start checking library update."""
		if self.library_thread and self.library_thread.is_running():
			return

		for mission in self.mission_manager.library.values():
			mission.set("state", "ANALYZE_INIT")

		mission = self.get_mission_to_check_update()
		if mission:
			self.library_thread = self.create_child(analyze).start(mission)

	def add_mission_update(self):
		"""Add updated mission to download list."""
		missions = self.mission_manager.get_by_state(
			"library", ("UPDATE",), all=True
		)
		self.mission_manager.add("view", *missions)

	def clean_finished(self):
		"""Remove finished missions."""
		missions = self.mission_manager.get_by_state(
			"view", ("FINISHED",), all=True
		)
		self.mission_manager.remove("view", *missions)

def console_download(url, savepath):
	"""Download url to savepath."""
	mission = Mission(url=url)
	Worker.sync(analyze, mission, pass_instance=True)
	Worker.sync(download, mission, savepath, pass_instance=True)

def console_init():
	"""Console init."""
	from docopt import docopt

	arguments = docopt(__doc__, version="Comic Crawler v" + __version__)

	if arguments["domains"]:
		print("Supported domains:\n" + ", ".join(list_domain()))

	elif arguments["gui"]:
		from .gui import MainWindow
		MainWindow().run()

	elif arguments["download"]:
		console_download(arguments["URL"], arguments["savepath"])

	elif arguments["migrate"]:
		from .migrate import migrate
		migrate()
