==============
Usage examples
==============

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

Since the run time is aligned to a tick integer multiple (in this example
tick = 0.1), it is to be noted that the system time - run time difference
is randomly set in the range 0.0-0.1, depending on the istant of time in which
the example is started. Then this quantity varies slightly for program execution
delays.
