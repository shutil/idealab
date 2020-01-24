from flask import Flask
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect
from routes.db import get_data
app = Flask(__name__)
app.config['SECRET_KEY'] = "THIS IS A SECRET"
socketio = SocketIO(app)
csrf = CSRFProtect(app)
# routes
from routes.index import *

# socket_programming
@socketio.on('gd')
def gd(name):
    print(name)

    ar = get_data()
    pl = []
    idea = []
    by = []

    for x in ar:
        pl.append(x[1])
        idea.append(x[2])
        by.append(x[3])
    socketio.emit('gd',{"pl":pl[::-1],"idea":idea[::-1],"by":by[::-1]},broadcast=True)
if __name__ == "__main__":
    socketio.run(app,debug=True,port=8000)