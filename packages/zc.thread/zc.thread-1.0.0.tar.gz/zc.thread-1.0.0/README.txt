Thread-creation helper
**********************

The thread-creation API provided by the Python ``threading`` module is
annoying. :)

This package provides a very simple thread-creation API that:

- Makes threads daemonic and allows daemonicity to be passed to the
  constructor.  For example::

    zc.thread.Thread(mythreadfunc)

  Starts a daemonic thread named ``'mythreadfunc'`` running
  ``mythreadfunc``.

- Allows threads to be defined via decorators, as in::

    import zc.thread

    @zc.thread.Thread
    def mythread():
        ...

  In the example above, a daemonic thread named ``mythread`` is
  created and started.  The thread is also assigned to the variable
  ``mythread``.

  You can control whether threads are daemonic and wether they are
  started by default::

    import zc.thread

    @zc.thread.Thread(daemon=False, start=False)
    def mythread():
        ...

- After a thread finishes, you can get the return value of the
  target function from the thread's ``value`` attribute, or, if the
  function raises an exception, you can get the exception object from
  the thread's ``exception`` attribute. (This feature was inspired by
  the same feature in gevent greenlets.)

- If a thread raises an exception (subclass of Exception), the
  exception is logged and a traceback is printed to standard error.

- A restart argument can be used to rerun a thread target function if
  there's an uncaught exception.  Value passed to the restart argument
  is passed to time.sleep before restarting the function.

There's also a Process constructor/decorator that works like Thread,
but with multi-processing processes, and without the ``value`` and
``exception`` attributes.

Changes
*******

1.0.0 (2015-06-17)
==================

- Python 3 support

- Thread names now include a function's module name.

- Unhandled exceptions in thread and process targets are now logged
  and printed with tracebacks.

- A restart argument can be used to automatically restart thread
  targets after a rest.

0.1.0 (2011-11-27)
==================

Initial release
