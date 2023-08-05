====================
nagios-load-per-core
====================
Installation
------------
Installation is simple:

::
   
   pip install nagios-load-per-core

Alternatively:

::

   git clone https://github.com/carlf/nagios-load-per-core.git
   python setup.py install

Usage
-----
Simply call with warning and critical values. Please note that the
load average is normalized such that it is divided by the number of
cores on the host.

::
   
   ./nagios-load-per-core -w 1.3 -c 2.4
