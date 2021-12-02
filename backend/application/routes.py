from application import app, db
from application.models import Country, Player
from flask import render_template, request, redirect, url_for, Response, jsonify
import os

#Countries

@app.route('/add/country', methods= ['POST'])
def add_country():
    package = request.json
    new_country = Country(country_name=package["country_name"])
    db.session.add(new_country)
    db.session.commit()
    return Response(f'Added New Country: {new_country.country_name}', mimetype='text/plain')

@app.route('/read/allcountries', methods=["GET"])
def read_all_countries():
    all_countries = Country.query.all()
    
    countries_dict = {"countries": []}
    
    for country in all_countries:
        players = []
        for player in country.players:
            players.append({"id" : player.id, "player_name" : player.player_name})
        countries_dict ["countries"].append(
            {
                "id": country.id,
                "country_name": country.country_name,
                "players": players 
                
            }
        )
    return jsonify(countries_dict)

@app.route('/read/country/<int:id>', methods=["GET"])
def read_country(id):
    country = Country.query.get(id)
    return jsonify(
        {
            "id": country.id,
            "country_name": country.country_name,
        }
    )

@app.route('/read/country/<int:id>/players', methods=["GET"])
def read_players(id):
    players = Country.query.get(id).players
    package = {"players": []}
    for player in players:
        package["players"].append(
            {
                "id": player.id,
                "player_name": player.player_name,
                "country_id": player.country_id
            }
        )
    return jsonify(package)

@app.route('/update/country/<int:id>', methods=["PUT"])
def update_country(id):
    package = request.json
    country = Country.query.get(id)
    country.country_name = package["country_name"]
    db.session.commit()
    return Response(f'Country name: {country.country_name} updated sucessfully', mimetype='text/plain')

@app.route('/delete/country/<int:id>', methods=["DELETE"])
def delete_country(id):
    country = Country.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return Response(f'Task with (ID: {id}), description: {country.country_name} is deleted', mimetype='text/plain')

# Players

@app.route('/add/player/<int:country_id>', methods= ['POST'])
def add_player(country_id):
    package = request.json
    new_player = Player(player_name = package["player_name"], country_id = country_id)
    #new_player = Player(player_name = package["player_name"], country_id = package["country_id"])
    db.session.add(new_player)
    db.session.commit()
    return Response(f'Added New Player: {new_player.player_name}', mimetype='text/plain')

@app.route('/read/allplayers', methods=["GET"])
def read_all_players():
    all_players = Country.query.all()
    json = {"players": []}
    for player in all_players:
        json["players"].append(
            {
                "id": player.id,
                "player_name": player.player_name,
                "country_id": player.country_id
            }
        )
    return jsonify(json)

@app.route('/read/player/<int:id>', methods=["GET"])
def read_player(id):
    player = Player.query.get(id)
    return jsonify(
        {
            "id": player.id,
            "country_name": player.player_name,
        }
    )

@app.route('/update/player/<int:id>', methods=["PUT"])
def update_player(id):
    package = request.json
    player = Player.query.get(id)
    player.player_name = package["player_name"]
    db.session.commit()
    return Response(f'Player name: {player.player_name} updated sucessfully', mimetype='text/plain')

@app.route('/delete/player/<int:id>', methods=["DELETE"])
def delete_player(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return Response(f'Player : {player.player_name} is removed from the team', mimetype='text/plain')
