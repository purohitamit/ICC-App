from application import app
from flask import render_template, request, redirect, url_for, jsonify
from application.forms import TaskForm
import requests

backend_host = "todo-app_backend:5000"
@app.route('/')
@app.route('/home')
def home():
    all_countries = requests.get(f"http://{backend_host}/read/allcountries").json()
    return render_template('index.html', title = "Home", all_countries=all_countries["countries"])


@app.route('/add/country', methods= ['GET', 'POST'])
def add_country():
    form = CountryForm()
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/add/country", json={"country_name": form.country_name.data} )
        return redirect(url_for('home'))
    return render_template("create_form.html", title = "Add a new country", form=form)

@app.route('/delete/country/<int:id>')
def delete_country(id):
    response = requests.delete(f"http://{backend_host}/delete/country/{id}")
    return redirect(url_for('home'))


@app.route('/add/country', methods= ['GET', 'POST'])
def add_player():
    form = PlayerForm()
    all_countries=requests.get(f"http://{backend_host}/read/allcountries").json()
    for country in all_countries["countries"]:
        form.country.choices.append((country["id"], country["country_name"]))
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/add/player", json={"player_name": form.player_name.data} )
        return redirect(url_for('home'))
    return render_template("create_form.html", title = "Add a new Player", form=form)

@app.route('/delete/country/<int:id>')
def delete_player(id):
    response = requests.delete(f"http://{backend_host}/delete/player/{id}")
    return redirect(url_for('home'))


=
