Comic Crawler
=============

Comic Crawler 是用來扒圖的一支 Python
Script。擁有簡易的下載管理員、圖書館功能、 與方便的擴充能力。

Features
--------

-  Extendible module design.
-  Easy to use function grabhtml, grabimg.
-  Auto setup referer and other common headers.

Dependencies
------------

-  pyexecjs - to execute javascript.
-  pythreadworker - a small threading library.

Development Dependencies
------------------------

-  pypandoc - to convert markdown to rst.

下載和安裝（Windows）
---------------------

Comic Crawler is on
`PyPI <https://pypi.python.org/pypi/comiccrawler/2015.6.8>`__. 安裝完
python 後，可以直接用 pip 指令自動安裝。

Python
~~~~~~

你需要 Python 3.4 以上。安裝檔可以從它的
`官方網站 <https://www.python.org/>`__ 下載。

安裝時記得要選「Add python.exe to path」，才能使用 pip 指令。

Comic Crawler
~~~~~~~~~~~~~

在 cmd 底下輸入以下指令

::

    pip install comiccrawler

要更新時用

::

    pip install --update comiccrawler

Supported domains
-----------------

    chan.sankakucomplex.com comic.acgn.cc comic.ck101.com
    comic.sfacg.com danbooru.donmai.us deviantart.com exhentai.org
    g.e-hentai.org konachan.com manhua.dmzj.com tel.dm5.com
    www.8comic.com www.99comic.com www.comicvip.com www.dm5.com
    www.manhuadao.com www.pixiv.net yande.re

使用說明
--------

::

    Usage:
      comiccrawler domains
      comiccrawler download URL [--dest SAVE_FOLDER]
      comiccrawler gui
      comiccrawler (--help | --version)

    Commands:
      domains             列出支援的網址
      download URL        下載指定的 url
      gui                 啟動主視窗

    Options:
      --dest SAVE_FOLDER  設定下載目錄（預設為 "."）
      --help              顯示幫助訊息
      --version           顯示版本

圖形介面
--------

.. figure:: http://i.imgur.com/ZzF0YFx.png
   :alt: 主視窗

   主視窗

-  在文字欄貼上網址後點「加入連結」或是按 Enter
-  若是剪貼簿裡有支援的網址，且文字欄同時是空的，程式會自動貼上
-  對著任務右鍵，可以選擇把任務加入圖書館。圖書館內的任務，在每次程式啟動時，都會檢查是否有更新。

設定檔
------

::

    [DEFAULT]
    ; 設定下載完成後要執行的程式，會傳入下載資料夾的位置
    runafterdownload = 

    ; 啟動時自動檢查圖書館更新
    libraryautocheck = true

    ; 下載目的資料夾
    savepath = ~/comiccrawler/download

    ; 開啟 grabber 偵錯
    logerror = false

    ; 每隔 5 分鐘自動存檔
    autosave = 5

-  設定檔位於 ``%USERPROFILE%\comiccrawler\setting.ini``
-  執行一次 ``comiccrawler gui`` 後關閉，設定檔會自動產生

Module example
--------------

.. code:: python

    #! python3
    """
    This is an example to show how to write a comiccrawler module.

    """

    import re
    import comiccrawler.core

    # The header used in grabber method
    header = {}

    # Match domain
    domain = ["www.example.com", "comic.example.com"]

    # Module name
    name = "This Is an Example"

    # With noepfolder = True, Comic Crawler won't generate subfolder for each episode.
    noepfolder = False

    # Wait 5 seconds between each page
    rest = 5

    # Specific user settings
    config = {
        "user": "user-default-value",
        "hash": "hash-default-value"
    }

    def loadconfig():
        """This function will be called each time the config reloaded.
        """
        header["Cookie"] = "user={}; hash={}".format(config["user"], config["hash"])

    def gettitle(html, url):
        """Return mission title.

        Title will be used in saving filepath, so be sure to avoid duplicate title.
        """
        return re.search("<h1 id='title'>(.+?)</h1>", html).group(1)

    def getepisodelist(html, url):
        """Return episode list.

        The episode list should be sorted by date, latest at last, so the 
        downloader will download the oldest first.
        """
        base = re.search("(https?://[^/]+)", url).group(1)
        ms = re.findall("<a href='(.+?)'>(.+?)</a>", html)
        s = []
        for m in ms:    
            u, title = m
            e = comiccrawler.Episode()
            e.title = title
            e.firstpageurl = base + url
            s.append(e)
        return s

    """
    There are two methods to get images url. If you can get all urls from the 
    first page, then use getimgurls. If you have to download each pages to get
    image url, use getimgurl and nextpage functions.

    You should only use one of two methods. Never write getimgurls and getimgurl
    both.
    """

    def getimgurls(html, url):
        """Return the list of all images"""

        ms = re.findall("<img src='(.+?)'>", html)
        return [m[0] for m in ms]

    def getimgurl(html, page, url):
        """Return the url of the image"""

        return re.search("<img id='showimage' src='(.+?)'>", html).group(1)

    def getnextpageurl(page, html, url):
        """Return the url of the next page. Return '' if this is the last page.
        """

        r = re.search("<a id='nextpage' href='(.+?)'>next</a>", html)
        if r is None:
            return ""
        return r.group(1)

    def errorhandler(er, ep):
        """Downloader will call errorhandler if there is an error happened when
        downloading image. Normally you can just ignore this function.
        """
        pass

Author
------

-  eight eight04@gmail.com


