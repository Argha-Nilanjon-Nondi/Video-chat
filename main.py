from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/speaker/")
def speaker():
    return render_template("speaker.html")

@app.route("/listener/")
def listener():
    return render_template("listener.html")

@socketio.on('send-data')
def handle_data(data):
    img=data["img"]
    socketio.emit("receive-data",data=img)
    # file=open("binary.png","w")
    # file.write(img)
    # file.close()
    # print(img)

if __name__ == '__main__':
    socketio.run(app,debug=True)