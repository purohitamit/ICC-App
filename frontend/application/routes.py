from application import app
from flask import render_template, request, redirect, url_for, jsonify
from application.forms import CountryForm, PlayerForm
import requests

backend_host = "icc-app_backend:5000"
@app.route('/')
@app.route('/home')
def home():
    all_countries = requests.get(f"http://{backend_host}/read/allcountries").json()["countries"]
    return render_template('index.html', title = "Home", all_countries = all_countries)


@app.route('/add/country', methods= ['GET', 'POST'])
def add_country():
    form = CountryForm()
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/add/country", json={"country_name": form.country_name.data} )
        return redirect(url_for('home'))
    return render_template("country_form.html", title = "Add a new country", form=form)

@app.route('/update/country/<int:id>', methods = ['GET', 'POST'])
def update_country(id):
    form = CountryForm()
    country = requests.get(f"http://{backend_host}/read/country/{id}").json()
    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/country/{id}", json={"country_name": form.country_name.data} )
        return redirect(url_for('home'))

    return render_template("update_country.html", country=country, form=form, title = "Update")

@app.route('/delete/country/<int:id>')
def delete_country(id):
    response = requests.delete(f"http://{backend_host}/delete/country/{id}")
    return redirect(url_for('home'))


@app.route('/add/player', methods= ['GET', 'POST'])
def add_player():
    form = PlayerForm()

    json = requests.get(f"http://{backend_host}/read/allcountries").json()
    for country in json["countries"]:
        form.country.choices.append((country["id"], country["country_name"]))
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/add/player/{form.country.data}", json={"player_name": form.player_name.data} )
        return redirect(url_for('home'))
    return render_template("player_form.html", title = "Add a new player", form=form)

@app.route('/update/player/<int:id>', methods = ['GET', 'POST'])
def update_player(id):
    form = PlayerForm()
    player = requests.get(f"http://{backend_host}/read/player/{id}").json()
    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/player/{id}", json={"player_name": form.player_name.data} )
        return redirect(url_for('home'))

    return render_template("update_player.html", player=player, form=form, title = "Update")

@app.route('/delete/player/<int:id>')
def delete_player(id):
    response = requests.delete(f"http://{backend_host}/delete/player/{id}")
    return redirect(url_for('home'))


