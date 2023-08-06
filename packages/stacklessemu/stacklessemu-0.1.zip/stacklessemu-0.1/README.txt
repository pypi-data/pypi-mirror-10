Installing `Stackless Python <http://www.stackless.com>`_ is a little cumbersome.  Wouldn't it be easier to install something resembling Stackless Python that upgrades your standard Python installation, with all it's installed site packages available as before?

This module bungs a greenlet-based module named ``stackless.py`` in place, so that anything expecting Stackless Python, will find this small approximation of Stackless Python instead. Whatever you are trying that requires Stackless Python may even work?  May be not though.

Limitations of this module:

* Arguments to ``stackless.run()`` are not supported.  This means that it does not do pre-emptive interruption of tasklets that have been running for a given number of opcodes.
* It cannot provide the module level properties that the official ``stackless`` module provides, like ``stackless.runcount``.
* It does not emulate the threading support, where each thread has an isolated scheduler, nor the interthread communications of tasklets and channels.

But the basic non-preemptive functionality is there.  It comes from, and has been used in the past as an alternative backend to the `syncless <https://pypi.python.org/pypi/syncless>`_ framework.  And maybe, at some time in the future the module will become more capable with your help?

Future direction: Use `tealets <https://bitbucket.org/stackless-dev/tealet>`_ as an alternative backend.
