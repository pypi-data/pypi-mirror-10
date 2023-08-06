Jmbo Video
==========
**Jmbo video application.**

.. figure:: https://travis-ci.org/praekelt/jmbo-video.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``jmbo-video`` to your Python path.

#. Add ``video`` to your ``INSTALLED_APPS`` setting.

#. Add (r'^video/', include('video.urls')) to urlpatterns.

#. Ensure ``<script src="http://jwpsrv.com/library/ivzA_hWZEeW5dgp+lcGdIw.js"></script>`` is in ``base.html``.

Notes on commercial usage
-------------------------

If you plan to use Jmbo Video commercially then you need to upgrade to a
commercial plan for JW Player. See http://www.jwplayer.com/.

Content types
-------------

Video
*****

A video has a richtext content field and points to a video stream.
