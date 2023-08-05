About
#####
Flask-BowerCDN is a `Flask`_ extension for making it easier to work with `Bower`_ in development and CDN content in production. It keeps the versions used in development in sync with those used in production without you having to manually edit your templates when you update a component.

Requirements
############
 * `Flask`_
 * `Flask-Bower`_

Installation
############

::

    pip install flask-bowercdn

Usage
#####
Simple usage:

::

    from flask import Flask
    from flask.ext.bowercdn import BowerCDN

    app = Flask(__name__)
    bowercdn = BowerCDN(app)

Or, for the application factory pattern:

::

    bowercdn = BowerCDN()
    bowercdn.init_app(app)

Now now you can use the ``bower_or_cdn`` function in your templates. Lets say, for example, that you installed `Bootstrap`_::

    <link rel="stylesheet" type="text/css" href="{{ bower_or_cdn('bootstrap/dist/css/bootstrap.css', '//maxcdn.bootstrapcdn.com/bootstrap/{version}/css/bootstrap.min.css') }}">

    <script type="text/javascript" src="{{ bower_or_cdn('bootstrap/dist/js/bootstrap.js', '//maxcdn.bootstrapcdn.com/bootstrap/{version}/js/bootstrap.min.js') }}"></script>

The ``bower_or_cdn`` function takes two argumnets: the first is a path as used by Flask-Bower and the second is a URL pattern. The important part of the pattern is the ``{version}`` variable which will be replaced by the installed version, as read from ``bower.json``, of said component.

What will happen is that when the app is run in debug or testing mode the local bower files will be used and when in production the CDN URL's will be used.

It is expected that you pin the versions in ``bower.json`` so you should use the ``-E`` parameter when installing bower components.

``bower_or_cdn`` can also be imported from ``flask.ext.bowercdn`` in case you need it in a view.

Options
#######
``BOWERCDN_BOWER_JSON``: The path to ``bower.json``. Defaults to ``'bower.json'``.

.. _Flask: http://flask.pocoo.org/
.. _Flask-Bower: https://github.com/lobeck/flask-bower
.. _bower: http://bower.io/
.. _bootstrap: http://getbootstrap.com/
