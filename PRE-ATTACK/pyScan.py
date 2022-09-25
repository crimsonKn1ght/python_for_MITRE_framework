#!/usr/bin/env python3

from tools.pyScanner import Scanner
from tools.DNSEnum import DNSScan
from args.arguments import argcheck

if __name__=="__main__":

	arguments = argcheck()
	args = arguments.Argcheck()

	if args.ports:
		ports = arg.ports
	else:
		ports = [22,25,53,80,443,445,8080,8443]

	if args.nums:
        	nums = arg.nums
	else:
		nums = False

	Scan = Scanner(args.host, ports)
	wrdlst = "wordlists/subdomains.txt"
	dictionary = []
	with open(wrdlst, "r") as f:
		dictionary = f.read().splitlines()
	Scanner = DNSScan(domain, dictionary, nums)


	try:
		Scan.SynScan()
		Scan.DNSScan()
		Scanner.SudomainSearch()
	except Exception as e:
		print(e)
