from application import app, db
from application.models import Tasks
from flask import render_template, request, redirect, url_for, Response, jsonify


#Countries

@app.route('/add/country', methods= ['POST'])
def add_country():
    package = request.json
    new_country = Countries(country_name=package["country_name"])
    db.session.add(new_country)
    db.session.commit()
    return Response(f'Added New Country: {new_country.country_name}', mimetype='text/plain')

@app.route('/view/allcountries', methods=["GET"])
def view_countries():
    all_countries = Countries.query.all()
    
    countries_dict = {"countries": []}
    
    for country in all_countries:
        countries_dict ["countries"].append(
            {
                "id": country.id,
                "country_name": country.country_name 
                
            }
        )
    return jsonify(countries_dict)

@app.route('/delete/country/<int:id>', methods=["DELETE"])
def delete_country(id):
    country = Countries.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return Response(f'Task with (ID: {id}), description: {country.country_name} is deleted', mimetype='text/plain')

# Players

@app.route('/add/player', methods= ['POST'])
def add_player():
    package = request.json
    new_player = Players(player_name=package["player_name"], country_id=package["country_id"])
    db.session.add(new_player)
    db.session.commit()
    return Response(f'Added New Player: {new_player.player_name}', mimetype='text/plain')

@app.route('/view/allplayers', methods=["GET"])
def view_players():
    all_players = Players.query.all()
    
    players_dict = {"players": []}
    
    for player in all_players:
        players_dict ["players"].append(
            {
                "id": player.id,
                "player_name": player.player_name 
                
            }
        )
    return jsonify(players_dict)

@app.route('/delete/player/<int:id>', methods=["DELETE"])
def delete_player(id):
    player = Players.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return Response(f'Player : {player.player_name} is removed from the team', mimetype='text/plain')
