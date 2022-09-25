#!/usr/bin/env python

import signal, sys


def terminated(signum, frame):
	pass


if __name__=='__main__':

	signal.signal(signal.SIGTERM, terminated)
	signal.signal(signal.SIGINT, terminated)

	while True:
		siginfo = signal.sigwaitinfo({signal.SIGINT, signal.SIGTERM})
		with open("terminated.txt", "w") as file:
			file.write("Process terminated by %d\n" % siginfo.si_pid)
		sys.exit(0)
