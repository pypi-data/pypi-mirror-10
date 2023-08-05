Project Free TV API
-------------------

This project offers APIs to explore the site `Project Free
TV <http://www.free-tv-video-online.me/>`__. You can use it to extract
links which can be used with
`Youtube-dl <https://github.com/rg3/youtube-dl/>`__.

|Downloads| |Wheel Status| |License|

Get it
~~~~~~

Install with ``pip install project-free-tv``,

Or,

Get the source code and just run ``python setup.py install``

Usage
~~~~~

To search for a show you need an instance of ProjectFreeTV.

.. code:: python


    from freetv import ProjectFreeTV

    # create an instance of the site
    pft = ProjectFreeTV()

    # search shows with trans in their titles

    pft.search_show("trans")

    Are you looking for one of these?

    Beast Wars Transformers
    Transformers
    Transformers Animated
    Transformers Armada
    Transformers Cyberton
    Transformers Energon
    Transformers Prime
    Transformers Robots In Disguise
    Transparent
    Transporter The Series

Right now it also lists movies with the keyword

You actually don't need an instance of ProjectFreeTV to get an instance
of a show but make sure it's on the site

.. code:: python

    # create an instance of the show Transparent
    show = ProjectFreeTV.get_show("Transparent")

    # or show = ProjectFreeTV.get_show("transparent")

    # get the number of seasons in the show
    show.seasons

    1

    show.season_urls

    {'Season 1': 'http://free-tv-video-online.me/internet/transparent/season_1.html'}

There are two kinds of links. The first one called ``online links`` is
the one you use to watch a show on Project Free TV. The second one
called ``downloadable links`` can be used with ``youtube-dl`` to
download shows.

.. code:: python

    # get the online links to watch episode 1 of season 1 of Transparent on Project Free TV
    show.get_online_links(1, 1)

    ['http://www.free-tv-video-online.me/player/novamov.php?id=2b6129bbaf87f',
    'http://www.free-tv-video-online.me/player/videoweed.php?id=6fea72bc35a70',
    'http://www.free-tv-video-online.me/player/divxstage.php?id=ldegt4109696v',
    'http://www.free-tv-video-online.me/player/movshare.php?id=1dd76cb937036',
    'http://www.free-tv-video-online.me/player/nowvideo.php?id=a9317f4711bc0',
    'http://www.free-tv-video-online.me/player/vodlocker.php?id=vf7sg4yobxlo',
    'http://www.free-tv-video-online.me/player/gorillavid.php?id=ju364s3hg50k',
    'http://www.free-tv-video-online.me/player/video.php?id=4f7TGDapj',
    'http://www.free-tv-video-online.me/player/allmyvideos.php?id=6n9my9wjh8u3',
    'http://www.free-tv-video-online.me/player/vidspot.php?id=g23mslq9fvd6',
    'http://www.free-tv-video-online.me/player/vidto.php?id=i5aoop614rkg']

    # some (but not all) of the links can be used with youtube-dl
    show.downloadable_episode_links(1,1)

    ['http://www.novamov.com/video/2b6129bbaf87f',
    'http://www.videoweed.es/file/6fea72bc35a70',
    'http://www.cloudtime.to/video/ldegt4109696v',
    'http://www.movshare.net/1dd76cb937036',
    'http://www.nowvideo.ch/video/a9317f4711bc0',
    'http://www.vodlocker.com/vf7sg4yobxlo',
    'http://www.gorillavid.com/ju364s3hg50k',
    'http://www.video.com/4f7',
    'http://allmyvideos.net/6n9my9wjh8u3',
    'http://www.vidspot.net/g23mslq9fvd6',
    'http://vidto.me/i5aoop614rkg']

The ``get_latest_episodes`` method returns the online links to the
latest three episodes of a show.

Example
~~~~~~~

A script that makes use of the APIs to download the latest three
episodes of several TV shows is under the directory ``examples``.

Dependency
~~~~~~~~~~

| This project depends on ``requests`` and ``lxml``.
| The example script in the examples directory also used
  `subliminal <https://github.com/Diaoul/subliminal>`__ to download
  subtitles. You should install it from source because the version from
  ``pip`` is outdated.
| The example script also used ``Youtube-dl`` to download videos.

Contribute
~~~~~~~~~~

Feel free to contribute to this project as much improvement can be done.
Any feedback is also greatly appreciated.

.. |Downloads| image:: https://pypip.in/download/project-free-tv/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/project-free-tv/
.. |Wheel Status| image:: https://pypip.in/wheel/project-free-tv/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/project-free-tv/
.. |License| image:: https://pypip.in/license/project-free-tv/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/project-free-tv/
