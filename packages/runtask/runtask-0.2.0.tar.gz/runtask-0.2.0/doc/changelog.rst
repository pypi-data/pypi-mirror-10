Changes
*******

Release 0.2.0 (released 29-Apr-2015)
====================================

New features
------------
* Run time speed: set the scheduling time flowing speed with respect to system
  time.
* Run time phase: add an offset to the scheduling time.
* Method task_info, if task has a finite run count, it returns also the
  current run number. Otherwise, it returns -1.
* Extended example to show counted runs and RunTask stopping. 

Incompabible changes
--------------------
* RunTask class, removed time argument. 
* Method task_data changed name to task_info.

Internals
---------
* New method _time, run time computation.
* Method _set, removed, partially replaced by method _time.

Fixes
-----
* Method stop, errata call to _set, corrige call to set.

Documentation
-------------
* Updated to 0.2.0


Release 0.1.0 (released 16-Feb-2015)
====================================

Changes
-------
* First release.
