from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from os import *

app = Flask('')
app.config['UPLOAD_PATH'] = '/'

@app.route('/', methods=['POST','GET'])
def home():
  return render_template("form.html")
    
def run():
  app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()

""" @TODO: wip """
def upload_file():
    uploaded_file = request.files['file']
    uploaded_file.save(uploaded_file.filename)
    
    return redirect(url_for('form.html'))