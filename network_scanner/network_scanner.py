#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #or in 2 lines
    #arp_request.pdst=ip
    print(arp_request.summary())
    #list properties of ARP object
    #scapy.ls(scapy.ARP())

scan("10.0.2.2/24")
