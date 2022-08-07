#!/usr/bin/env python3

from scapy.all import *

class Scanner():
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports

    def SynScan(self):
        # we can set different flags here be swapping "S" with "A" for ack scan, etc
        ans, unans = sr(IP(dst=self.host)/TCP(sport=5555, dport=self.ports, flags="S"), timeout=2, verbose=0)
        print("Open ports at %s:" %self.host)
        # s for sent packet and r for recieved packet
        for (s,r,) in ans:
            if s[TCP].dport == r[TCP].sport:
                print(s[TCP].dport)

    def DNSScan(self):
        # rd is for setting num of DNS requests; DNSQR is for DNS Query
        ans,unans = sr(IP(dst=self.host)/UDP(sport=5555, dport=53)/DNS(rd=1, qd=DNSQR(qname="google.com")), timeout=2, verbose=0)
        if ans:
            print("DNS server at %s" %self.host)

