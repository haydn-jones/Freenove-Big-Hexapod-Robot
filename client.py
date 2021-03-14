import socketio

sio = socketio.Client()
app = socketio.WSGIApp(sio)

@sio.event
def connect():
    print("connected")
    sio.emit("message", "oogabooga")

@sio.event
def disconnect(sid):
    print("disconnected")

sio.connect("http://127.0.0.1:5000")
sio.wait()