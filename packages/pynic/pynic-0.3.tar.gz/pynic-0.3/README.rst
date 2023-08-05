# pyNIC
A Python interface to get Network Interface Cards(NIC) information on Linux.

## Dependencies

You must install the Python headers.

On Debian and Ubuntu:

    $ sudo apt-get install python-dev

## Installation

    sudo python setup.py install

## Usage

    import pynic

You can see some examples in examples directory.

## Functions

    get_list_interfaces()               -   It lists all available interfaces

## Iface class

This class store all necessary information about the interfaces.

### Attributes

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

### Methods

    set_broad_addr(String)              -   Set a new IPv4 Broadcast Address to the NIC (You must have root permission)
    set_inet_addr(String)               -   Set a new IPv4 Address to the NIC (You must have root permission)
    set_inet_mask(String)               -   Set a new IPv4 Mask Address to the NIC (You must have root permission)
    update_tx_rx()                      -   Update NIC's TX/RX information (bytes and packets)

### Class Methods

    Iface.get_interface(String)         -   It return an Iface object with all information about it
