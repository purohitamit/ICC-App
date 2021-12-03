from application import app
from application.routes import backend_host
from flask import url_for
from flask_testing import TestCase
import requests_mock

test_data = {
    "id": 1,
    "country_name": "Test Country 1",
    "players": [
        {
            "id": 1,
            "player_name": "Test Player",
            "country_id": 1
        }
    ]
}

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):

    def test_home_read(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/allcountries", json={'countries': []})
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_add_country(self):
        response = self.client.get(url_for('add_country'))
        self.assert200(response)
      
        

class TestHome(TestBase):

    def test_home_read_allcountries(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/allcountries", json={'countries': [test_data]})
            response = self.client.get(url_for('home'))
            self.assertIn("Test Country 1", response.data.decode("utf-8"))
            
    
class TestAddCountry(TestBase):

    def test_add_country_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/add/country", text="Test response")
            m.get(f"http://{backend_host}/read/allcountries", json={'countries': [test_data]})
            response = self.client.post(url_for('add_country'), follow_redirects=True)
            self.assertIn("Test Country 1", response.data.decode("utf-8"))

class TestAddPlayer(TestBase):

    def test_add_player_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/add/player/1", text="Test response")
            m.get(f"http://{backend_host}/read/allcountries", json={'countries': [test_data]})
            response = self.client.post(url_for('add_player'), follow_redirects=True, json={"country": 1, "player_name": "Test Player 2"})
            self.assertIn("Test Country 1", response.data.decode("utf-8"))
    
