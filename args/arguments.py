#!/usr/bin/env python3

import argparse
import sys


class argcheck:
	def __init__(self):
		self.example=\
		f'example: python {sys.argv[0]} -H 192.168.0.1\n    	python {sys.argv[0]} -H 127.0.0.1 -p [22,25,53,80]'

	def Argcheck(self):
		parser = argparse.ArgumentParser(description="Tool for port scanning and DNS Enumeration", usage=f"python {sys.argv[0]} -H <host> -p <ports>", epilog=self.example, formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-H', '--host', metavar='', dest='host', help='Enter host to scan')
		parser.add_argument('-p', '--ports', metavar='', dest='ports', help='Enter ports to scan')
		args = parser.parse_args()

		if not args.host:
			parser.print_help()
			sys.exit()

		return args

