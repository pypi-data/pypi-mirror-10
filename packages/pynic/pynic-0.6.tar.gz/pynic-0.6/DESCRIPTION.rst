pyNIC
=======

This project is an interface written using C Python API to provide information
about Network Interface Cards.

Documentation
=============

Currently, all documentation can be accessed in project's GitHub page.

Dependencies
============

You must install the Python headers.

On Debian and Ubuntu:

    $ sudo apt-get install python-dev

Installation
============

    sudo python setup.py install

Support
=======

This project should support Python 2.x and 3.x in every Linux. However, 
it was tested only on Python 2.7 and 3.4.

What's new
===========
- Support Python 3.x
- Added repr e str functions
- Fixed some bugs
- Increased reliability
- Added functions to change addresses

What's new 0.5
==============
- Removed set functions
- Added getter and setter as class properties
- Added constants

What's new 0.6
==============
- Added setter for name
- Added hardware address validation for both length format
- Added setter for hardware address, but it is working just for 17 length format
