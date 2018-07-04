#!/usr/bin/env python

import subprocess
while True:
	process = subprocess.Popen(['ping', '-w', '3', '-i', '0.2', '-s', '65500', '192.168.49.87'])
	process.wait()
	output = process.poll()

	if output == 0:
		print("connected")
		break
		print("no connection")

run_node = subprocess.Popen(['./comm.sh'])

