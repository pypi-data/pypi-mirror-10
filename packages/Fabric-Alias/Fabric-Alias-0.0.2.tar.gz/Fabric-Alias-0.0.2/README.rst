==============
 fabric-alias
==============

you can alias fabric commands in fabfile

Install
=======
::

    easy_install fabric-alias
    # or
    pip install fabric-alias

Useage
======

In your __init__.py in the fabfile directory like `~/fabfile/__init__.py`, write like this ::

    from . import SOME_YOUR_MODULE
    from fablic_alias import set_alias
    set_alias({"sym": SOME_YOUR_MODULE})

So you can run sym command instead of SOME_YOUR_MODULE ::

    $ fab sym
    # usually you type fab SOME_YOUR_MODULE
    # but this is too long to type
