#!/usr/bin/env python3

import subprocess
while True:
	process = subprocess.Popen(['ping','google.com', '-c', '4', '-W', '1'], stdout = subprocess.PIPE)
	process.wait()
	output = process.poll()

	if output == 0:
		print("Connected")
		subprocess.call(["rsync", "-avz", "-e", " 'ssh'", "/home/iiitd/Desktop/test neelabhro@192.168.1.22:/home/neelabhro/Desktop"])
	else:
		print("no connection")

