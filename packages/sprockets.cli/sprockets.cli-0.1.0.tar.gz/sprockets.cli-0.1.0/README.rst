sprockets.cli
=============
The sprockets CLI interface for running applications. Applications are meant
to be run by a controller that is managed by the sprockets CLI interface.

The sprockets CLI interface loads controller applications that are registered
using setuptools entry points.

|Version| |Downloads| |Status| |Coverage| |License|

Example CLI Usage
-----------------

Help:

.. code::

    # sprockets --help

    usage: sprockets [-h] [--apps] [--plugins] [-e [PLUGIN]] [-s] [-v] [--version]
                     CONTROLLER ... [APP]

    Command line tool for starting a Sprockets application

    positional arguments:
      CONTROLLER            Available sprockets application controllers
        http                HTTP Application Controller
        amqp                RabbitMQ Worker Controller
      APP                   Application to run

    optional arguments:
      -h, --help            show this help message and exit
      --apps                List installed applications
      --plugins             List installed plugins
      -e [PLUGIN], --enable [PLUGIN]
                            Enable a plugin
      -s, --syslog          Log to syslog
      -v, --verbose         Verbose logging output, use -vv for DEBUG level
                            logging
      --version             show program's version number and exit

    Find more Sprockets controllers and plugins at
    https://sprockets.readthedocs.org

Starting a Web App with the NewRelic plugin:

.. code::

    # sprockets -e newrelic http my_web_app

Controllers
-----------

Each controller is expected to expose at least a ``main(application, args)``
method that would be invoked when starting the application. Additional, a
controller can implement a ``add_cli_arguments(parser)`` method that will be
invoked when setting up the command line parameters. This allows controllers
to inject configuration directives into the cli.

Controller API Summary:

.. code:: python

    module.add_cli_arguments(ArgumentParser)     # optional
    module.main(app_module, argparse.Namespace)

Plugins
-------

Plugins are able to inject themselves at multiple points in the application
lifecycle. Plugins that implement a ``initialization(controller)`` method will
see that method invoked before a controller is started.  In addition, if a
``on_startup(controller)`` method is defined, it will be invoked after a
Controller has started a application. Finally if a ``on_shutdown(controller)``
method is defined, it will be invoked when a controller has shutdown.

Plugin API Summary:

.. code:: python

    plugin.initialize(controller_module)   # optional
    plugin.on_start(controller_module)     # optional
    plugin.on_shutdown(controller_module)  # optional

Example Entrypoints
-------------------

Controller:

.. code:: python

    {'sprockets.controller': ['http=sprockets.controllers.http:None']},

Application:

.. code:: python

    {'sprockets.http.app': ['app-name=package.or.module:None']}

(Replace ``app-name`` with the name of your application)

Applications
------------

Applications can be a python package or module and if they are registered
to a specific controller, can be referenced by an alias. Application contracts
vary by controller.

.. |Version| image:: https://badge.fury.io/py/sprockets.cli.svg?
   :target: http://badge.fury.io/py/sprockets.cli

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.cli.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.cli

.. |Coverage| image:: https://coveralls.io/repos/sprockets/sprockets.cli/badge.png
   :target: https://coveralls.io/r/sprockets/sprockets.cli
  
.. |Downloads| image:: https://pypip.in/d/sprockets.cli/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.cli
   
.. |License| image:: https://pypip.in/license/sprockets.cli/badge.svg?
   :target: https://sprockets.readthedocs.org
