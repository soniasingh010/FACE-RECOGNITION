import mimetypes
from urllib import response
from webbrowser import get
from flask import Flask, render_template
from pkg_resources import yield_lines
from camera import video

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
        b'content-Type: image/jpeg\r\n\r\n' + frame +
        b'\r\n\r\n')    

@app.route('/video')

def video():
    return response(gen(video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)