from application import app
from flask import render_template, request, redirect, url_for, jsonify
from application.forms import TaskForm
import requests

backend_host = "todo-app_backend:5000"
@app.route('/')
@app.route('/home')
def home():
    all_tasks = requests.get(f"http://{backend_host}/read/allTasks").json()
    return render_template('index.html', title = "Home", all_tasks=all_tasks["tasks"])


@app.route('/create/task', methods= ['GET', 'POST'])
def create_task():
    form = TaskForm()
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/task", json={"description": form.description.data} )
        return redirect(url_for('home'))
    return render_template("create_form.html", title = "Add a new task", form=form)



@app.route('/update/task/<int:id>', methods = ['GET', 'POST'])
def update_task(id):
    form = TaskForm()
    task = requests.get(f"http://{backend_host}/read/task/{id}").json()
    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/task/{id}", json={"description": form.description.data} )
        return redirect(url_for('home'))

    return render_template("update_task.html", task=task, form=form, title = "Update")


@app.route('/delete/task/<int:id>')
def delete_task(id):
    response = requests.delete(f"http://{backend_host}/delete/task/{id}")
    return redirect(url_for('home'))

@app.route('/complete/task/<int:id>')
def complete_task(id):
    response = requests.put(f"http://{backend_host}/complete/task/{id}")
    return redirect(url_for('home'))

@app.route('/incomplete/task/<int:id>')
def incomplete_task(id):
    response = requests.put(f"http://{backend_host}/incomplete/task/{id}")
    return redirect(url_for('home'))

