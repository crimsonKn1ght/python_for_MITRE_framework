#!/usr/bin/env python

import pathlib


def getTimestamps(filename):
	fname = pathlib.Path(filename)
	stats = fname.stat()
	if not fname.exists():
		return []
	return(stats.st_ctime, stats.stats_mtime, stats.stats_atime)

def checkTimestamps(filename, create, modify, access):
	stats = getTimestamps(filename)
	if len(stats) == 0:
		return False
	(ctime, atime, mtime) = stats
	if float(create) != float(ctime):
		return False
	elif float(modify) != float(mtime):
		return False
	elif float(access) != float(atime):
		return False
	return True

def checkDecoyFiles():
	with open("decoys.txt", "r") as file:
		for line in file:
			vals = line.rstrip().split(',')
			if not checkTimestamps(vals[0], vals[1], vals[2], vals[3]):
				print("%s has been tampered." % (vals[0]))


if __name__=='__main__':

	checkDecoyFiles()
