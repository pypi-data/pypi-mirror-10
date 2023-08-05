==============
Usage examples
==============

Using the system time
=====================

Simple example
--------------
This simple example is based on the the execution of 3 tasks. The task #0 is
run every 5 seconds, at second beginning, forever. The task #1
is run every second, at the middle of second, forever. The task #2 is run
every second, at the middle of second, for 5 times.
Each task printouts its task id, nominal runtime and delay of real runtime
from nominal runtime, the difference runtime - system time. Task #2 prints
also the run number.
Since all these tasks make the same output, they all can be inplemented by only
one function, the "task" function.

.. literalinclude:: ../examples/example.py
    :linenos:
    :language: python
    :lines: 30-

This an excerpt from example output. Task with 5 second period has id=0.
Tasks with 1 second period have respectively id=1 and id=2.
 
.. literalinclude:: ../examples/example.out
    :linenos:

It is to be noted that the difference sys-runtime that is the difference
between the system time at task call and the nominal run time is always
below 0.2 ms. This difference measures the scheduling overhead introduced
by RunTask


Capabilities of the periodic timing
-----------------------------------
This example shows almost all capabilities of the periodic timing. Task #0
is run 15 second after the beginning of each minute, forever. Task #1 is
run immediately every 5 seconds.

.. literalinclude:: ../examples/timecap.py
    :linenos:
    :language: python
    :lines: 30-

This an excerpt from example output. Task with 1 minute period has id=0.
Task with 5 second period has id=1.
 
.. literalinclude:: ../examples/timecap.out
    :linenos:

Task #1 that is run immediately, shows an initial run delay of about 0.02s
due to the initial program setup. Since the time has tick=0.1, task #1 starts
on a random time aligned with a tick multiple.
