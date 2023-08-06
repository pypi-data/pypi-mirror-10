********************
collective.js.cycle2
********************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

`Cycle2`_ is a versatile slideshow plugin for jQuery built around ease-of-use.
It supports a declarative initialization style that allows full customization without any scripting.
Simply include the plugin, declare your markup, and Cycle2 does the rest.

This package adds a browser resource to use Cycle2 and its plugins on a Plone site.

.. _`Cycle2`: http://jquery.malsup.com/cycle2/

Mostly Harmless
===============

.. image:: https://secure.travis-ci.org/collective/collective.js.cycle2.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.js.cycle2

.. image:: https://coveralls.io/repos/collective/collective.js.cycle2/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/collective/collective.js.cycle2

.. image:: https://pypip.in/d/collective.js.cycle2/badge.png
    :alt: Downloads
    :target: https://pypi.python.org/pypi/collective.js.cycle2

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.js.cycle2

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Usage
-----

If your page template inherits from ``main_template``,
just include the resources on it by usign the following syntax::

    <metal:block fill-slot="javascript_head_slot">
      <script src="++resource++collective.js.cycle2/jquery.cycle2.min.js"
          tal:attributes="src string:$portal_url/++resource++collective.js.cycle2/jquery.cycle2.min.js"></script>
    </metal:block>

Alternatively you can add them into your site's JavaScript Registry directly or by using GenericSetup::

    <?xml version="1.0"?>
    <object name="portal_javascripts">
      <javascript
          cacheable="True" compression="none" cookable="True" enabled="True"
          id="++resource++collective.js.cycle2/jquery.cycle2.min.js" />
    </object>

Plugins
-------

The package also includes the code for the following plugins:

* Transition
    * Carousel
    * Flip
    * IE-Fade
    * ScrollVert
    * Shuffle
    * Tile
* Functional
    * Caption2
    * Center
    * Swipe
    * YouTube

Check Cycle2 `download page`_ for more information.

.. _`download page`: http://jquery.malsup.com/cycle2/download/

Not entirely unlike
===================

`collective.js.galleria`_
    Galleria is a JavaScript image gallery framework built on top of the jQuery library.
    The aim is to simplify the process of creating professional image galleries for the web and mobile devices.

.. _`collective.js.galleria`: https://pypi.python.org/pypi/collective.js.galleria
