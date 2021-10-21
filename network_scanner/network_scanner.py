#!/usr/bin/env python

#https://scapy.readthedocs.io/en/latest/
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #srp send_receive_packet returns answered and unanswered 
    scapy.srp(arp_request_broadcast)
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary()) 


scan("10.0.2.2/24")
