from application import app
from flask import render_template, request, redirect, url_for, jsonify
from application.forms import TaskForm
import requests

backend_host = "todo-app_backend:5000"
@app.route('/')
@app.route('/home')

@app.route('/add/country', methods= ['GET', 'POST'])




@app.route('/delete/country/<int:id>')
def delete_task(id):
    response = requests.delete(f"http://{backend_host}/delete/task/{id}")
    return redirect(url_for('home'))
