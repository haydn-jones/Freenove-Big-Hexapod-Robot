import socketio
import eventlet

sio = socketio.Server(always_connect=True, cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid: str, environ: dict):
    print(sid, "connected")

@sio.event
def disconnect(sid):
    print("disconnected")

@sio.event
def message(name: str, data: str):
    print(data)

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)