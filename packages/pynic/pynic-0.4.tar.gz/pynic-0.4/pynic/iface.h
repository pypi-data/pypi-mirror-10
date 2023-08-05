#ifndef IFACE_H
#define IFACE_H

#ifndef _GNU_SOURCE
#define _GNU_SOURCE     /* To get defns of NI_MAXSERV and NI_MAXHOST */
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

#include <ifaddrs.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/if.h>
#include <linux/if_link.h>

#define HW_ADDR_LENGTH 18
#define IFACE_NAME_LENGTH 10
#define MAX_IFACE 10

struct iface{
    char *name;
    char *inet_addr;
    char *inet6_addr;
    char *hw_addr;
    char *broad_addr;
    char *inet_mask;
    char *inet6_mask;
    unsigned char running;
    unsigned char updown;
    unsigned int flags;
    unsigned int mtu;
    unsigned int metric;
    unsigned int tx_bytes;
    unsigned int rx_bytes;
    unsigned int tx_packets;
    unsigned int rx_packets;
};

void free_iface(struct iface *ifa);
void init_iface(struct iface *ifa);
int get_info_interface(struct iface* ifa, const char *name_iface);
int get_list_interfaces(char *** list_ifaces);
char * get_mac(const char *name_iface);
int set_broad_addr(struct iface *ifa, const char *broad_addr);
int set_flags(struct iface *ifa, int flags);
int set_hw_addr(struct iface *ifa, const char *hw_addr);
int set_inet_addr(struct iface *ifa, const char *inet_addr);
int set_inet_mask(struct iface *ifa, const char *inet_mask);
int update_tx_rx(struct iface* ifa);

#endif
