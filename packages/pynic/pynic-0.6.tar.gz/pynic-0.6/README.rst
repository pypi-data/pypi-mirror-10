pyNIC
=====

A Python interface to get Network Interface Cards(NIC) information on Linux.

Dependencies
============
You must install the Python headers.

On Debian and Ubuntu:

::

    $ sudo apt-get install python-dev

Installation
============

::

    sudo python setup.py install

Usage
=====

::

    import pynic

You can see an example at the end of this page.

Functions
=========

::    

    get_list_interfaces()               -   It lists all available interfaces

Constants
=========

Many constants from netdevice were exported to this module.
You can check the documentation on http://man7.org/linux/man-pages/man7/netdevice.7.html

Currently, the constants which you are able to use are:

::

    IFF_UP                              -   Interface is running.
    IFF_BROADCAST                       -   Valid broadcast address set.
    IFF_DEBUG                           -   Internal debugging flag.
    IFF_LOOPBACK                        -   Interface is a loopback interface.
    IFF_POINTOPOINT                     -   Interface is a point-to-point link.
    IFF_RUNNING                         -   Resources allocated.
    IFF_NOARP                           -   No arp protocol, L2 destination address not set.
    IFF_PROMISC                         -   Interface is in promiscuous mode.
    IFF_NOTRAILERS                      -   Avoid use of trailers.
    IFF_ALLMULTI                        -   Receive all multicast packets.
    IFF_MASTER                          -   Master of a load balancing bundle.
    IFF_SLAVE                           -   Slave of a load balancing bundle.
    IFF_MULTICAST                       -   Supports multicast
    IFF_PORTSEL                         -   Is able to select media type via ifmap.
    IFF_AUTOMEDIA                       -   Auto media selection active.
    IFF_DYNAMIC                         -   The addresses are lost when the interface goes down.
    IFF_LOWER_UP                        -   Driver signals L1 up (since Linux 2.6.17)
    IFF_DORMANT                         -   Driver signals dormant (since Linux 2.6.17)
    IFF_ECHO                            -   Echo sent packets (since Linux 2.6.25)

Iface class
===========

This class store all necessary information about the interfaces.

Attributes
==========

::

    String  name                        -   Interface's name
    String  inet_addr                   -   Interface's IPv4 address
    String  inet6_addr                  -   Interface's IPv6 address
    String  hw_addr                     -   Interface's MAC address
    String  broad_addr                  -   Interface's Broadcast address
    String  inet_mask                   -   Interface's Network Mask v4 address
    String  inet6_mask                  -   Interface's Network Mask v6 address
    Boolean running                     -   Indicates if interface is running or not
    Boolean updown                      -   Indicates if interfaces is Up or Down
    Integer flags                       -   Other Interface's flags
    Integer tx_bytes                    -   Amount of bytes that the interface transmitted
    Integer rx_bytes                    -   Amount of bytes that the interface received
    Integer tx_packets                  -   Amount of packets that the interface transmitted
    Integer rx_packets                  -   Amount of packets that the interface received

Methods
=======

::
    
    update_tx_rx()                      -   Update NIC's TX/RX information (bytes and packets)

Class Methods
=============

::    

    Iface.get_interface(String)         -   It returns an Iface object with all information about it

Examples
========

- Get an interface and set a new IPv4 Address (You must execute as root)

::

    import pynic
    
    interface = pynic.Iface.get_interface('eth0')
    interface.inet_addr = "192.168.0.100"
    print(interface.inet_addr) #Print the new address

You can see more examples in the example directory.
