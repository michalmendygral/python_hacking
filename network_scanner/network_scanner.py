#!/usr/bin/env python

#https://scapy.readthedocs.io/en/latest/
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #srp send_receive_packet returns answered and unanswered 
    scapy.srp(arp_request_broadcast)
    l_answered = scapy.srp(arp_request_broadcast, timeout=1, verbose= False)[0]
    l_targets = []
    
    for answer in l_answered:
        d_target = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        l_targets.append(d_target)

    return l_targets

def print_result(result_list):
    print('IP\t\tMAC\n-------------------------------------')
    for client in result_list:
        print(client["ip"] + "\t" + client["mac"])
    print('-------------------------------------')

scan_result = scan("10.0.2.2/24")
print_result(scan_result)
