import signal
from Server.Server import *
from Server.Control import *
from Server.Thread import stop_thread

class ServerControl:
	def __init__(self):
		self.server = Server()

		self.server.turn_on_server()
		self.server.tcp_flag = True
		self.video = threading.Thread(target = self.server.transmission_video)
		self.video.start()
		self.instruction = threading.Thread(target = self.server.receive_instruction)
		self.instruction.start()

	def close(self, *args, **kwargs):
		print("Shutting down threads...")
		try:
			stop_thread(self.video)
			stop_thread(self.instruction)
		except:
			pass

		print("Shutting down sockets...")
		try:
			self.server.server_socket.shutdown(2)
			self.server.server_socket1.shutdown(2)
			self.server.turn_off_server()
		except:
			pass
		exit(0)

if __name__ == '__main__':
	server = ServerControl()
	signal.signal(signal.SIGINT, server.close)
