===============================
        python-manhole
===============================

| |docs| |travis| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-manhole/badge/?style=flat
    :target: https://readthedocs.org/projects/python-manhole
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/python-manhole/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-manhole

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-manhole?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-manhole

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/python-manhole/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-manhole

.. |landscape| image:: https://landscape.io/github/ionelmc/python-manhole/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-manhole/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/manhole.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/manhole

.. |downloads| image:: http://img.shields.io/pypi/dm/manhole.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/manhole

.. |wheel| image:: https://pypip.in/wheel/manhole/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/manhole

.. |supported-versions| image:: https://pypip.in/py_versions/manhole/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/manhole

.. |supported-implementations| image:: https://pypip.in/implementation/manhole/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/manhole

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-manhole/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-manhole/

Manhole is in-process service that will accept unix domain socket connections and present the
stacktraces for all threads and an interactive prompt. It can either work as a python daemon
thread waiting for connections at all times *or* a signal handler (stopping your application and
waiting for a connection).

Access to the socket is restricted to the application's effective user id or root.

This is just like Twisted's `manhole <http://twistedmatrix.com/documents/current/api/twisted.manhole.html>`__.
It's simpler (no dependencies), it only runs on Unix domain sockets (in contrast to Twisted's manhole which
can run on telnet or ssh) and it integrates well with various types of applications.

:Documentation: http://python-manhole.readthedocs.org/en/latest/

Usage
=====

Install it::

    pip install manhole

You can put this in your django settings, wsgi app file, some module that's always imported early etc:

.. code-block:: python

    import manhole
    manhole.install() # this will start the daemon thread

    # and now you start your app, eg: server.serve_forever()

Now in a shell you can do either of these::

    netcat -U /tmp/manhole-1234
    socat - unix-connect:/tmp/manhole-1234
    socat readline unix-connect:/tmp/manhole-1234

Socat with readline is best (history, editing etc).

Sample output::

    $ nc -U /tmp/manhole-1234

    Python 2.7.3 (default, Apr 10 2013, 06:20:15)
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> dir()
    ['__builtins__', 'dump_stacktraces', 'os', 'socket', 'sys', 'traceback']
    >>> print 'foobar'
    foobar

Alternative client
------------------

There's a new experimental ``manhole`` bin since 1.1.0, that emulates ``socat``::

    usage: manhole [-h] [-t TIMEOUT] [-1 | -2] PID

    Connect to a manhole.

    positional arguments:
      PID                   A numerical process id, or a path in the form:
                            /tmp/manhole-1234

    optional arguments:
      -h, --help            show this help message and exit
      -t TIMEOUT, --timeout TIMEOUT
                            Timeout to use. Default: 1 seconds.
      -1, -USR1             Send USR1 (10) to the process before connecting.
      -2, -USR2             Send USR2 (12) to the process before connecting.



Features
========

* Uses unix domain sockets, only root or same effective user can connect.
* Can run the connection in a thread or in a signal handler (see ``oneshot_on`` option).
* Can start the thread listening for connections from a signal handler (see ``activate_on`` option)
* Compatible with apps that fork, reinstalls the Manhole thread after fork - had to monkeypatch os.fork/os.forkpty for
  this.
* Compatible with gevent and eventlet with some limitations - you need to either:

  * Use ``oneshot_on``, *or*
  * Disable thread monkeypatching (eg: ``gevent.monkey.patch_all(thread=False)``, ``eventlet.monkey_patch(thread=False)``

* The thread is compatible with apps that use signalfd (will mask all signals for the Manhole threads).

Options
-------

.. code-block:: python

    manhole.install(
        verbose=True,
        verbose_destination=2,
        patch_fork=True,
        activate_on=None,
        oneshot_on=None,
        sigmask=manhole.ALL_SIGNALS,
        socket_path=None,
        reinstall_delay=0.5,
        locals=None,
        strict=True,
    )

* ``verbose`` - Set it to ``False`` to squelch the logging.
* ``verbose_destination`` - Destination for verbose messages. Set it to a file descriptor or handle. Default is
  unbuffered stderr (stderr ``2`` file descriptor).
* ``patch_fork`` - Set it to ``False`` if you don't want your ``os.fork`` and ``os.forkpy`` monkeypatched
* ``activate_on`` - Set to ``"USR1"``, ``"USR2"`` or some other signal name, or a number if you want the Manhole thread
  to start when this signal is sent. This is desireable in case you don't want the thread active all the time.
* ``oneshot_on`` - Set to ``"USR1"``, ``"USR2"`` or some other signal name, or a number if you want the Manhole to
  listen for connection in the signal handler. This is desireable in case you don't want threads at all.
* ``sigmask`` - Will set the signal mask to the given list (using ``signalfd.sigprocmask``). No action is done if
  ``signalfd`` is not importable. **NOTE**: This is done so that the Manhole thread doesn't *steal* any signals;
  Normally that is fine cause Python will force all the signal handling to be run in the main thread but signalfd
  doesn't.
* ``socket_path`` - Use a specifc path for the unix domain socket (instead of ``/tmp/manhole-<pid>``). This disables
  ``patch_fork`` as children cannot resuse the same path.
* ``reinstall_delay`` - Delay the unix domain socket creation *reinstall_delay* seconds. This alleviates
  cleanup failures when using fork+exec patterns.
* ``locals`` - Names to add to manhole interactive shell locals.
* ``daemon_connection`` - The connection thread is daemonic (dies on app exit). Default: ``False``.
* ``redirect_stderr`` - Redirect output from stderr to manhole console. Default: ``True``.
* ``strict`` - If ``True`` then ``AlreadyInstalled`` will be raised when attempting to install manhole twice. Default: ``True``.

Environment variable installation
---------------------------------

Manhole can be installed via the ``PYTHONMANHOLE`` environment varialbe.

This::

    PYTHONMANHOLE='' python yourapp.py

Is equivalent to having this in ``yourapp.py``:

    import manhole
    manhole.install()

Any extra text in the environment variable is passed to ``manhole.install()``. Example::

    PYTHONMANHOLE='onshot_on="USR2"' python yourapp.py

What happens when you actually connect to the socket
----------------------------------------------------

1. Credentials are checked (if it's same user or root)
2. ``sys.__std*__``/``sys.std*`` are be redirected to the UDS
3. Stacktraces for each thread are written to the UDS
4. REPL is started so you can fiddle with the process

Known issues
============

* Using threads and file handle (not raw file descriptor) ``verbose_destination`` can cause deadlocks. See bug reports:
  `PyPy <https://bitbucket.org/pypy/pypy/issue/1895/writing-to-stderr-from-multiple-processes>`_ and `Python 3.4
  <http://bugs.python.org/issue22697>`_.

SIGTERM and socket cleanup
--------------------------

By default Python doesn't call the ``atexit`` callbacks with the default SIGTERM handling. This makes manhole leave stray
socket files around. If this is undesirable you should install a custom SIGTERM handler so ``atexit`` is properly invoked.

Example:

.. code-block:: python

    import signal
    import sys

    def handle_sigterm(signo, frame):
        sys.exit(128 + signo)  # this will raise SystemExit and cause atexit to be called

    signal.signal(signal.SIGTERM, handle_sigterm)

Requirements
============

:OS: Linux, OS X
:Runtime: Python 2.6, 2.7, 3.2, 3.3, 3.4 or PyPy

Similar projects
================

* Twisted's `old manhole <http://twistedmatrix.com/documents/current/api/twisted.manhole.html>`__ and the `newer
  implementation <http://twistedmatrix.com/documents/current/api/twisted.conch.manhole.html>`__ (colors, serverside
  history).
* `wsgi-shell <https://github.com/GrahamDumpleton/wsgi-shell>`_ - spawns a thread.
* `pyrasite <https://github.com/lmacken/pyrasite>`_ - uses gdb to inject code.
* `pydbattach <https://github.com/albertz/pydbattach>`_ - uses gdb to inject code.
* `pystuck <https://github.com/alonho/pystuck>`_ - very similar, uses `rpyc <https://github.com/tomerfiliba/rpyc>`_ for
  communication.
* `pyringe <https://github.com/google/pyringe>`_ - uses gdb to inject code, more reliable, but relies on `dbg` python
  builds unfortunatelly.
* `pdb-clone <https://pypi.python.org/pypi/pdb-clone>`_ - uses gdb to inject code, with a `different strategy
  <https://code.google.com/p/pdb-clone/wiki/RemoteDebugging>`_.
