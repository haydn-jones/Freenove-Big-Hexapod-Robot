import time
import sys
import signal
from Server.Servo import *

# Main program logic follows:
if __name__ == '__main__':
	S = Servo()
	def signal_handler(sig, frame):
		print("Interrupted! Relaxing Legs")
		S.relax()
		sys.exit(-1)
	signal.signal(signal.SIGINT, signal_handler)
	for i in range(32):
		S.setServoAngle(i, 90)
	signal.pause()
