pyWorker
========
A threading framework written in python. Help you build threaded app.

This module was originally included in eight04/ComicCrawler.

Features
--------
* Pause, resume, stop, restart thread.
* Create child thread.
* Create async tasks.
* Communicate between threads with Message.

Known issues
------------
* If there is an error in `worker.sync`, the error message will be printed
  twice, once in the child thread and once in the parent.

