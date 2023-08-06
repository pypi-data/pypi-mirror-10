=============================
sitechantment
=============================

.. image:: https://travis-ci.org/mmessmore/sitechantment.png?branch=master
    :target: https://travis-ci.org/mmessmore/sitechantment

.. image:: https://pypip.in/d/sitechantment/badge.png
    :target: https://pypi.python.org/pypi/sitechantment


Check a site for spelling errors in a way that can be integrated with your testing

Why?
----

I wanted a way to add spellchecking to a suite of tests for a Flask-based
site.  I saw some windows tools, using a combination of lynx/curl/wget and
i/a/hunspell.

But I just want a way to get a +/- test and a list of misspelled words.

How
---

So sitechantment is a command line utility to do just that.  You can pass it a url
to crawl, an optional additional list of words, language, etc.  It will crawl the
site (not wandering off to another host/port) spellcheck every page and give you a
list of words that are "misspelled".

You have the ability to run with a --update flag to automatically add all words to
a personal word list so they aren't flagged on the next run.

It is also available as a class sitechantment.SiteCheck, that can be used inside a
test suite.  You can even pass it a flask test client instead of using requests
and be able to crawl a site inside of py.test or whatever is being used to unit
test a flask application.  (Really anything can be used as long as it supports
handling uri's with a get() method).
