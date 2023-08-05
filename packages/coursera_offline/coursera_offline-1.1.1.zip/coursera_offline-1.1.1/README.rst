Coursera Offline
================

Download and save the video lectures of your favorite courses for
offline viewing.

Contents
========

-  `Installation`_
-  `Proxy Settings`_
-  `Requires`_
-  `Running`_
-  `Features`_
-  `Full Usage`_
-  `Some sample invocations`_
-  `First time download`_
-  `Obtaining the shortname`_
-  `Synching`_
-  `Auto Synch`_
-  `Fetch using file`_

Installation
------------

-  Make sure you have python version 2.7 installed. If you don’t have
   python, get it from `here`_
-  If you have python and are not sure of the version, type
   ``python -V`` in the terminal. If it says 2.7.x+ then you may proceed
   to the next instruction. Otherwise, go to the link provided above.
-  Install ``pip`` using ``sudo apt-get install python-pip``. Install
   the application using ``sudo pip install coursera_offline``
-  Before proceeding to the next step, make sure you have ``setuptools``
   module installed. If it isn’t, you can find the installation
   instructions
   `here <https://pypi.python.org/pypi/setuptools#installation-instructions>`__.
-  If you don’t want to install pip, you can download the tar.gz from
   `PyPi`_ or zip from `Github`_, extract the archive file and follow
   the installation instructions in the README.txt file.
-  You may also clone the repo onto your local workstation and follow
   the instructions in the README.txt file
   ``git clone https://github.com/sanketh95/coursera-offline``

For those behind proxy
^^^^^^^^^^^^^^^^^^^^^^

You just need to set ``HTTP_PROXY`` and ``HTTPS_PROXY`` environment
variables and python automatically sends all requests through proxy.
Here’s the way to set proxy in windows and linux

Windows
'''''''

Run ``set HTTP_PROXY=http://user:password@address:port`` and
``set HTTPS_PROXY=https://user:password@address:port``

Linux
'''''

Run ``export HTTP_PROXY=http://user:password@address:port`` and
``export HTTPS_PROXY=https://user:password@address:port``

REQUIRES
~~~~~~~~

-  Python2.7
-  pyquery 1.2.9
-  crontab 1.8.1

**Note:** You need not install the requirements manually, the setup
script takes care of installing them for you.

Running
-------

Windows
~~~~~~~

-  Open command prompt and change the ``cd`` into the directory
   containing **coursera-offline** and run
   ``python coursera_offline -h``

Linux
~~~~~

-  Open terminal and run ``coursera_offline -h``.

Features
--------

-  All the videos are downloaded according to the folder structure and
   you don’t need to take care of sorting the videos into separate
   folders manually.
-  You need not track the order of the videos/weeks as the script
   intentionally rename

.. _Installation: #installation
.. _Proxy Settings: #for-those-behind-proxy
.. _Requires: #requires
.. _Running: #running
.. _Features: #features
.. _Full Usage: #full-usage
.. _Some sample invocations: #some-sample-invocations
.. _First time download: #first-time-download
.. _Obtaining the shortname: #obtaining-the-shortname
.. _Synching: #synching
.. _Auto Synch: #auto-synch
.. _Fetch using file: #fetch-using-file
.. _here: https://www.python.org/download/releases/2.7/
.. _PyPi: https://pypi.python.org/packages/source/c/coursera_offline/coursera_offline-0.1.0.tar.gz
.. _Github: https://github.com/sanketh95/coursera-offline/archive/master.zip