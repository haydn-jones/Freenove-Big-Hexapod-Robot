# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Server.Server import *
from Server.Control import *

class MyWindow:
	def __init__(self):
		self.user_ui = True
		self.start_tcp = False
		self.server = Server()

		self.server.turn_on_server()
		self.server.tcp_flag = True
		self.video = threading.Thread(target = self.server.transmission_video)
		self.video.start()
		self.instruction = threading.Thread(target = self.server.receive_instruction)
		self.instruction.start()

	def closeEvent(self, event):
		try:
			stop_thread(self.video)
			stop_thread(self.instruction)
		except:
			pass
		try:
			self.server.server_socket.shutdown(2)
			self.server.server_socket1.shutdown(2)
			self.server.turn_off_server()
		except:
			pass
		os._exit(0)

if __name__ == '__main__':
	myshow = MyWindow()
	try:
		pass
	except KeyboardInterrupt:
		myshow.closeEvent(myshow)
