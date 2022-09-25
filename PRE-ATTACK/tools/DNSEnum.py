#!/usr/bin/env python3

import dns
import dns.resolver
import socket


class DNSScan():
    def __init__(self, domain, dictionary, nums):
        self.domain = domain
        self.dictionary = dictionary
        self.nums = nums

    def ReverseDNS(self, ip):
        try:
            result = socket.gethostbyaddr(ip)
        except:
            return []
        return [result[0]] + result[1]

    def DNSRequest(self, domain):
        try:
            result = dns.resolver.resolve(domain, 'A')
            if result:
                print(domain)
                for answer in result:
                    print(answer)
                    print("Domain names: %s" % self.ReverseDNS(answer.to_text()))
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            return

    def SubdomainSearch(self):
        for word in dictionary:
            subdomain = word + "." + self.domain
            self.DNSRequest(subdomain)
            if self.nums:
                for i in range(0, 10):
                    s = word + str(i) + "." + self.domain
                    self.DNSRequest(s)

