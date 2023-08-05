#include "iface.h"

void free_iface(struct iface *ifa){
    free(ifa->name);
    free(ifa->inet_addr);
    free(ifa->inet6_addr);
    free(ifa->hw_addr);
}

void init_iface(struct iface *ifa){
    ifa->name = malloc(sizeof(char)*IFNAMSIZ);
    (ifa->name)[0] = '\0';
    ifa->inet_addr = malloc(sizeof(char)*NI_MAXHOST);
    (ifa->inet_addr)[0] = '\0';
    ifa->inet6_addr = malloc(sizeof(char)*NI_MAXHOST);
    (ifa->inet6_addr)[0] = '\0';
    ifa->hw_addr = malloc(sizeof(char)*HW_ADDR_LENGTH);
    (ifa->hw_addr)[0] = '\0';
    ifa->inet_mask = malloc(sizeof(char)*NI_MAXHOST);
    (ifa->inet_mask)[0] = '\0';
    ifa->inet6_mask = malloc(sizeof(char)*NI_MAXHOST);
    (ifa->inet6_mask)[0] = '\0';
    ifa->broad_addr = malloc(sizeof(char)*NI_MAXHOST);
    (ifa->broad_addr)[0] = '\0';
    
    ifa->running = 0;
    ifa->updown = 0;
    
    ifa->mtu = 0;
    ifa->metric = 0;
    
    ifa->tx_bytes = 0;
    ifa->rx_bytes = 0;
    ifa->tx_packets = 0;
    ifa->rx_packets = 0;
}

int get_info_interface(struct iface* ifa, const char *name_iface){
    struct ifaddrs *ifaddr, *aux;
    struct rtnl_link_stats *stats;
    int find = -1;
    
    init_iface(ifa);
    
    if (getifaddrs(&ifaddr) == -1) {
        return -1;
    }
    
    for(aux=ifaddr; aux!=NULL; aux=aux->ifa_next){
        if (aux->ifa_addr == NULL){
            continue;
        }
        
        if(strcmp(aux->ifa_name, name_iface) == 0){
            if(aux->ifa_addr->sa_family == AF_PACKET){
                find = 0;
                strcpy(ifa->name, aux->ifa_name);
                ifa->hw_addr = get_mac(name_iface);
                
                if(aux->ifa_flags & IFF_RUNNING){
                    ifa->running = 1;
                }
                
                if(aux->ifa_flags & IFF_UP){
                    ifa->updown = 1;
                }
                
                ifa->flags = aux->ifa_flags;
                
                stats = aux->ifa_data;

                ifa->tx_bytes =  stats->tx_bytes;
                ifa->rx_bytes =  stats->rx_bytes;
                ifa->tx_packets =  stats->tx_packets;
                ifa->rx_packets =  stats->rx_packets;
            }else if(aux->ifa_addr->sa_family == AF_INET){
                getnameinfo(aux->ifa_addr, sizeof(struct sockaddr_in),
                            ifa->inet_addr, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
                getnameinfo(aux->ifa_netmask, sizeof(struct sockaddr_in),
                            ifa->inet_mask, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
                getnameinfo(aux->ifa_ifu.ifu_broadaddr, sizeof(struct sockaddr_in),
                            ifa->broad_addr, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
            }else if(aux->ifa_addr->sa_family == AF_INET6){
                getnameinfo(aux->ifa_addr, sizeof(struct sockaddr_in6),
                            ifa->inet6_addr, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
                getnameinfo(aux->ifa_netmask, sizeof(struct sockaddr_in6),
                            ifa->inet6_mask, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
            }
        }
    }
    freeifaddrs(ifaddr);
    
    return find;
}

int get_list_interfaces(char *** list_ifaces){
    char **aux_list_ifaces;
    struct ifaddrs *ifaddr, *ifa;
    int i = 0;
    int j = 0;

    aux_list_ifaces = malloc(sizeof(char*)*MAX_IFACE);

    if (getifaddrs(&ifaddr) == -1) {
        return -1;
    }
   
    for(ifa=ifaddr; ifa!=NULL; ifa=ifa->ifa_next){
        if (ifa->ifa_addr == NULL){
            continue;
        }
        
        for(j=0; j<i; j++){
            /*
             * Check if it already exists the interface inside the list
             */
            if(strcmp(ifa->ifa_name, aux_list_ifaces[j]) == 0){
                break;
            }
        }
        
        if(j < i){
            /*
             * If j < i, it means that last loop was broken before it finishes
             * Then, it means that was found a equal string inside the list
            */
            continue;
        }
        
        aux_list_ifaces[i] = malloc(sizeof(char)*IFACE_NAME_LENGTH);
        strcpy(aux_list_ifaces[i], ifa->ifa_name);
        i++;
    }
    
    *list_ifaces = aux_list_ifaces;
    
    freeifaddrs(ifaddr);
    
    return j+1;
}

char * get_mac(const char *name_iface){
    //TODO Try to simplify this function
    int i;
    char *ret = malloc(sizeof(char)*HW_ADDR_LENGTH);
    struct ifreq s;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);

    strcpy(s.ifr_name, name_iface);
    if (fd >= 0 && ret && 0 == ioctl(fd, SIOCGIFHWADDR, &s)){
        for(i=0; i<6; ++i){
            sprintf(ret+i*3, "%02x",(unsigned char) s.ifr_addr.sa_data[i]);
            if(i < 5){
                sprintf(ret+2+i*3,":");
            }
        }
    }else{
        return NULL;
    }
    return ret;
}

int set_broad_addr(struct iface *ifa, const char *broad_addr){
    struct ifreq ifr;
    struct sockaddr_in* addr = (struct sockaddr_in*)&ifr.ifr_addr;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;

    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_addr.sa_family = AF_INET;
    
    if(inet_pton(AF_INET, broad_addr, &addr->sin_addr) == 0){
        result = -1;
    }
    
    if(result == 0 && ioctl(fd, SIOCSIFBRDADDR, &ifr) == -1){
        result = errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }
    
    close(fd);
    
    return result;
}

int set_flags(struct iface *ifa, int flags){
    struct ifreq ifr;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;

    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_addr.sa_family = AF_INET;
    
    ifr.ifr_flags = flags;
    if(ioctl(fd, SIOCSIFFLAGS, &ifr) == -1){
        return errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }
    
    close(fd);
    
    return result;
}

int set_hw_addr(struct iface *ifa, const char *hw_addr){
    /*
     * This function validates the hardware address before to call
     * the real function to set the new hardware address. This function 
     * accepts both formats, 12 and 17 length.
     */
    char hw_modified[17];
    if(validate_hw_addr(hw_addr)){            
        if(strlen(hw_addr) == 12){
            normalize_hw_addr(hw_addr, hw_modified);
            printf("%s\n", hw_modified);
        }else{
            strcmp(hw_modified, hw_addr);
            printf("%s\n", hw_modified);
        }
        
        return SET_HW_ADDR(ifa, hw_modified);
    }
    
    return 0;    
}

int SET_HW_ADDR(struct iface *ifa, const char *hw_addr){
    /*
     * This function is the real one which set the hardware address.
     * However the hardware address must be in the formatted with 12 legth.
     * So, I encourage you to use the set_hw_addr() function.
     */
    
    /* 
     * TODO Try to understand why is not working when I use normalized.
     */
    
    struct ifreq ifr;
    
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;

    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_hwaddr.sa_family = ARPHRD_ETHER;

    sscanf(hw_addr, "%hhx:%hhx:%hhx:%hhx:%hhx:%hhx",
            &ifr.ifr_hwaddr.sa_data[0],
            &ifr.ifr_hwaddr.sa_data[1],
            &ifr.ifr_hwaddr.sa_data[2],
            &ifr.ifr_hwaddr.sa_data[3],
            &ifr.ifr_hwaddr.sa_data[4],
            &ifr.ifr_hwaddr.sa_data[5]
            );
    
    if(ioctl(fd, SIOCSIFHWADDR, &ifr) == -1){
        result = errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }

    close(fd);
    
    return result;
}

int set_inet_addr(struct iface *ifa, const char *inet_addr){
    struct ifreq ifr;
    struct sockaddr_in* addr = (struct sockaddr_in*)&ifr.ifr_addr;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;
    
    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_addr.sa_family = AF_INET;
    if(inet_pton(AF_INET, inet_addr, &addr->sin_addr) == 0){
        /*
         * It is a invalid IPv4 address
         */
        result = -1;
    }
    
    if(result == 0 && ioctl(fd, SIOCSIFADDR, &ifr) == -1){
        result = errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }
    
    close(fd);
    
    return result;
}

int set_inet_mask(struct iface *ifa, const char *inet_mask){
    struct ifreq ifr;
    struct sockaddr_in* addr = (struct sockaddr_in*)&ifr.ifr_addr;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;

    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_addr.sa_family = AF_INET;
    
    if(inet_pton(AF_INET, inet_mask, &addr->sin_addr) == 0){
        /*
         * It is a invalid IPv4 address
         */
        result = -1;
    }
    
    if(result == 0 && ioctl(fd, SIOCSIFNETMASK, &ifr) == -1){
        result = errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }
    
    close(fd);
    
    return result;
}

int set_name(struct iface *ifa, const char *name){
    struct ifreq ifr;
    int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
    int result = 0;

    strncpy(ifr.ifr_name, ifa->name, IFNAMSIZ);
    ifr.ifr_addr.sa_family = AF_INET;
    
    strcpy(ifr.ifr_newname, name);
    if(ioctl(fd, SIOCSIFNAME, &ifr) == -1){
        return errno;
    }
    
    if(result == 0){
        get_info_interface(ifa, ifa->name);
    }
    
    close(fd);
    
    return result;
}

int update_tx_rx(struct iface* ifa){
    //TODO Verify errors
    
    struct ifaddrs *ifaddr, *aux;
    struct rtnl_link_stats *stats;
    
    if (getifaddrs(&ifaddr) == -1) {
        return -1;
    }
    
    for(aux=ifaddr; aux!=NULL; aux=aux->ifa_next){
        if (aux->ifa_addr == NULL){
            continue;
        }
        
        if(strcmp(aux->ifa_name, ifa->name) == 0){
            if(aux->ifa_addr->sa_family == AF_PACKET){
                stats = aux->ifa_data;

                ifa->tx_bytes =  stats->tx_bytes;
                ifa->rx_bytes =  stats->rx_bytes;
                ifa->tx_packets =  stats->tx_packets;
                ifa->rx_packets =  stats->rx_packets;
                
                break;
            }
        }
    }
    freeifaddrs(ifaddr);
    
    return 0;
}

/* 
 * Help Functions 
 */
int validate_hw_addr(const char * hw_addr){
    int i = 0;
    int s = 0;

    while(*hw_addr){
        if (isxdigit(*hw_addr)) {
            i++;
        }else if(*hw_addr == ':' || *hw_addr == '-'){
            if (i == 0 || i/2-1 != s){
                break;              
            }
            s++;
        }else{
            s = -1;
        }
        hw_addr++;
    }

    return (i == 12 && (s == 5 || s == 0));
}

int normalize_hw_addr(const char * hw_addr, char hw_modified[]){
    /* Normalizes to 17 length format */
    
    sprintf(hw_modified, "%c%c:%c%c:%c%c:%c%c:%c%c:%c%c", 
            hw_addr[0], hw_addr[1], hw_addr[3], hw_addr[4],
            hw_addr[6], hw_addr[7], hw_addr[9], hw_addr[10],
            hw_addr[12], hw_addr[13], hw_addr[15], hw_addr[16]);
    
    return 1;
}
