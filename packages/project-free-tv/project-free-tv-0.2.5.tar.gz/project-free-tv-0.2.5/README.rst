Project Free TV
---------------

This project offers ways to explore the site `Project Free
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

    ['Beast Wars Transformers',
     'Transformers',
     'Transformers Animated',
     'Transformers Armada',
     'Transformers Cyberton',
     'Transformers Energon',
     'Transformers Prime',
     'Transformers Robots In Disguise',
     'Transformers Robots In Disguise (2015)',
     'Transparent',
     'Transporter The Series']

Right now it also lists movies with the keyword in their names.

To get an instance of a show you don't need an instance of
ProjectFreeTV.

.. code:: python

    # create an instance of the show Orphan Black, the case of the name doesn't matter.
    ob = ProjectFreeTV.get_show('orphan black')

    # get links for latest 2 episodes of the show
    ob.get_latest_episodes(2)
    [['http://allmyvideos.net/6w209e0ilx4y',
      'http://allmyvideos.net/ckb82t2wqcdp',
      'http://allmyvideos.net/vt3rb3z48xro',
      'http://www.mooshare.biz/1ybh2h7rbt57',
      'http://www.mooshare.biz/adkqf57ntv5d',
      'http://www.mooshare.biz/tu575xgbjio9',
      'http://www.movshare.net/video/fc716bb0cabd6',
      'http://www.novamov.com/video/07ab880176038',
      'http://www.nowvideo.ch/video/dab1b4f33de8c',
      'http://www.videoweed.es/file/6fe98f8c424bb',
      'http://www.vidspot.net/cer2h88l5k2r',
      'http://www.vidspot.net/kn6zt3o5twcu',
      'http://www.vidspot.net/mqjzsu9plw3q'],
     ['http://allmyvideos.net/m06rmgatnlqp',
      'http://allmyvideos.net/pqsneos7tzvs',
      'http://www.mooshare.biz/1zta6utfay0u',
      'http://www.mooshare.biz/cld1kyampv3p',
      'http://www.movshare.net/video/2fb604f462786',
      'http://www.novamov.com/video/98017f0ff9324',
      'http://www.nowvideo.ch/video/d58b8002c3ef7',
      'http://www.videoweed.es/file/c37a74b9100a0',
      'http://www.vidspot.net/cb10ys2yct8n',
      'http://www.vidspot.net/zckx70lune1n']]


    # create an instance of the show Breaking Bad
    show = pft.get_show('breaking bad')

    show.season_count
    5

    # get links for an episode
    show.get_ydl_links(season=3, episode=2)
    ['http://www.movshare.net/video/6a9e17b58bdc4',
     'http://www.movshare.net/video/l0vjyt7hxlayi',
     'http://www.novamov.com/video/d1230ae72ebb7',
     'http://www.novamov.com/video/yunibyknhh2ut',
     'http://www.nowvideo.ch/video/9cfd1845f0f34',
     'http://www.videoweed.es/file/341df227846db',
     'http://www.videoweed.es/file/a397e70c45f7a']

    # get links for a whole season
    show.get_ydl_links_for_season(5)
    {1: ['http://www.mooshare.biz/a4tt7rh5f5p7',
      'http://www.mooshare.biz/k6m2dxw6cfe7',
      'http://www.mooshare.biz/l9611uymszr4',
      'http://www.mooshare.biz/y3mhbsv9zgqy',
      'http://www.mooshare.biz/znx0bn9rjzma',
      'http://www.novamov.com/video/jw2css68j11gn',
      'http://www.nowvideo.ch/video/d0676087fb70f',
      'http://www.nowvideo.ch/video/d0676087fb70f'],
     2: ['http://www.mooshare.biz/7yxpwt8zybd4',
      'http://www.mooshare.biz/9ionebould0u',
      'http://www.mooshare.biz/ff2ntzkutl3b',
      'http://www.mooshare.biz/kx7fumuvzczi',
      'http://www.mooshare.biz/llzwbwtotcqd',
      'http://www.movshare.net/video/zz3r47nzzv1ww',
      'http://www.novamov.com/video/f363a44e634e1',
      'http://www.nowvideo.ch/video/0162cf1af5636',
      'http://www.videoweed.es/file/ccal473givib3'],
     3: ['http://www.mooshare.biz/3subibu2sa4m',
      'http://www.mooshare.biz/diig01hef3a4',
      'http://www.mooshare.biz/t2lgut5f7fk5',
      'http://www.mooshare.biz/til4eqb4kw4a',
      'http://www.mooshare.biz/xgnszpnxes39',
      'http://www.mooshare.biz/yzu6uo6d2n99',
      'http://www.movshare.net/video/618493115a60f'],
     4: ['http://www.mooshare.biz/4pk09qsv6peg',
      'http://www.mooshare.biz/8k5hth1wwc84',
      'http://www.mooshare.biz/a8fj447eivo7',
      'http://www.mooshare.biz/in1avq4oco7w',
      'http://www.mooshare.biz/j69bhqw6k0o5',
      'http://www.mooshare.biz/s8xq08jul0gu',
      'http://www.movshare.net/video/872d52b2d6720',
      'http://www.nowvideo.ch/video/35d6e90d7e5e4',
      'http://www.nowvideo.ch/video/aea79e12a4dfc',
      'http://www.videoweed.es/file/2e54d39e33071',
      'http://www.videoweed.es/file/b78fa9792e44c'],
     5: ['http://www.mooshare.biz/740haowo6d7i',
      'http://www.mooshare.biz/av08zl0ssu2b',
      'http://www.mooshare.biz/c0wk3gr5m2za',
      'http://www.mooshare.biz/ku1sdhn8si36',
      'http://www.mooshare.biz/mq8w96p44sct',
      'http://www.movshare.net/video/34a1f0672ca46',
      'http://www.nowvideo.ch/video/b0ba5b74f4acd'],
     6: ['http://www.mooshare.biz/0dm57i8kscbz',
      'http://www.mooshare.biz/5syv06nga4rt',
      'http://www.mooshare.biz/nj7w3wla5vx0',
      'http://www.mooshare.biz/stsc572dsl9l',
      'http://www.mooshare.biz/wh76r1gbwfey',
      'http://www.movshare.net/video/8a83619f139d5',
      'http://www.novamov.com/video/20c4e4c1f5c95',
      'http://www.nowvideo.ch/video/2862109ee12b5',
      'http://www.videoweed.es/file/396446dbd0eb1'],
     7: ['http://www.mooshare.biz/06lxtdsqhf0l',
      'http://www.mooshare.biz/ipc902bw8agk',
      'http://www.mooshare.biz/sc0zv9s8s2dd',
      'http://www.mooshare.biz/wxxmkueih4jq',
      'http://www.movshare.net/video/cf7c1dca79619',
      'http://www.nowvideo.ch/video/3121253839d7c',
      'http://www.videoweed.es/file/726478af27de6'],
     8: ['http://www.mooshare.biz/axeglnltsoft',
      'http://www.mooshare.biz/gpae4ts2tb76',
      'http://www.movshare.net/video/3cb646131cdcf',
      'http://www.nowvideo.ch/video/fbe957ced95fa',
      'http://www.videoweed.es/file/75713e72e94a4'],
     9: ['http://www.mooshare.biz/2fg3rqqsbu72',
      'http://www.mooshare.biz/70hqaxgbzqan',
      'http://www.mooshare.biz/822fhl0wn3tj',
      'http://www.mooshare.biz/a0pne1gv983d',
      'http://www.mooshare.biz/ddnh9eobql7n',
      'http://www.mooshare.biz/hq7g4uur8bxm',
      'http://www.mooshare.biz/olrditvdsmd1',
      'http://www.mooshare.biz/suxn3gg9p7mv',
      'http://www.mooshare.biz/tjtgiecrnrgv',
      'http://www.movshare.net/video/82f745085fd3d',
      'http://www.novamov.com/video/t52llt5qeqa90',
      'http://www.nowvideo.ch/video/37a390f4f3080',
      'http://www.videoweed.es/file/8c341a8aa2b3a'],
     10: ['http://www.mooshare.biz/5uz7p27k6vew',
      'http://www.mooshare.biz/ikdf7wufciah',
      'http://www.mooshare.biz/thx8he0i3jp2',
      'http://www.mooshare.biz/vbf6q42o290i',
      'http://www.mooshare.biz/w664fahllv3q',
      'http://www.mooshare.biz/w7dvubjfd9qn',
      'http://www.mooshare.biz/zkmut4xyt4c7',
      'http://www.movshare.net/video/88a2e9a228353',
      'http://www.novamov.com/video/92gb1hf01f7tg',
      'http://www.nowvideo.ch/video/e9119676eb6fb',
      'http://www.videoweed.es/file/f3536010f5825'],
     11: ['http://www.mooshare.biz/3aobloqpu810',
      'http://www.mooshare.biz/rta2d1iqm0yt',
      'http://www.mooshare.biz/v0x6558ghcv1',
      'http://www.mooshare.biz/va8tbfe2ms3r',
      'http://www.mooshare.biz/ziehuzmwusq1',
      'http://www.videoweed.es/file/deb000a1cbbe9'],
     12: ['http://www.mooshare.biz/0uy3j8ks5i8w',
      'http://www.mooshare.biz/db7gsmgxos02',
      'http://www.mooshare.biz/lkrxw41sxnyj',
      'http://www.mooshare.biz/nc9bm6dlf58f',
      'http://www.novamov.com/video/e1c6721b57368'],
     13: ['http://www.mooshare.biz/4lo24fy2l4lv',
      'http://www.mooshare.biz/l0v2l33dvex3',
      'http://www.mooshare.biz/sdkpshf71d91',
      'http://www.mooshare.biz/tiyqnxpuofw8',
      'http://www.novamov.com/video/d7b3fcaa8177a',
      'http://www.videoweed.es/file/66de25eb444cf'],
     14: ['http://www.mooshare.biz/3gw5cyl99def',
      'http://www.mooshare.biz/6b2y2deswp9l',
      'http://www.mooshare.biz/chsv9l6yh8jm',
      'http://www.mooshare.biz/onqh24pc3i8r',
      'http://www.mooshare.biz/wb53jiu0fm0w',
      'http://www.movshare.net/video/7184a8bf4c380',
      'http://www.videoweed.es/file/8c8c8945e8e03'],
     15: ['http://www.mooshare.biz/009zqn5zl8rn',
      'http://www.mooshare.biz/3eskcb56cly0',
      'http://www.mooshare.biz/xzjqmmxj0ngn',
      'http://www.videoweed.es/file/c737bc26f5fe9'],
     16: ['http://allmyvideos.net/2u5d5kf6jfen',
      'http://allmyvideos.net/qax5xf2xn4pp',
      'http://www.mooshare.biz/33o8penrrf8g',
      'http://www.mooshare.biz/80e6uaqtmuuw',
      'http://www.mooshare.biz/8fxzawlmg3b1',
      'http://www.mooshare.biz/c3ezpqbdc6ac',
      'http://www.mooshare.biz/h4s8ri5agyrb',
      'http://www.mooshare.biz/oqtuzh0nkc2v',
      'http://www.mooshare.biz/qfi6vq0bo4th',
      'http://www.movshare.net/video/adfc6b558bf01',
      'http://www.videoweed.es/file/cfdeff583830c',
      'http://www.vidspot.net/kz8t7o6ttz0l',
      'http://www.vidspot.net/tm2doxyad68j']}

Example
~~~~~~~

A script that makes use of the APIs to download the latest few episodes
of several TV shows is under the directory ``examples``.

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
