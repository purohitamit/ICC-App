from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import Country
from application.models import Player

test_country = {
                
                "id": 1,
                "country_name": "Country 1",
                "players": []
                
            }
test_player = {
                "id": 1,
                "player_name": "Player 1",
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()
        db.session.add(Country(country_name="Country 1"))
        db.session.commit()


    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):
    def test_read_all_countries(self):
        response = self.client.get(url_for("read_all_countries"))
        all_countries = { "countries" : [test_country]}
        self.assertEquals(all_countries, response.json)

    def test_read_country(self):
        response = self.client.get(url_for("read_country", id = 1))
        json = {"country_name": "Country 1", "id": 1}
        self.assertEquals(json, response.json)

class TestCreate(TestBase):
    def test_add_country(self):
        response = self.client.post(
            url_for("add_country"),
            json ={"country_name": "Testing add functionality"},
            follow_redirects=True
        )
        self.assertEquals(b"Added New Country: Testing add functionality", response.data)
       
class TestUpdate(TestBase):
    def test_update_country(self):
        response = self.client.put(
            url_for("update_country", id=1),
            json ={"country_name": "Testing update functionality"}
        )
        self.assertEquals(b"Updated Country ID: 1 ", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.delete(url_for("delete_country", id=1))
        self.assertEquals(b"Deleted Country with ID: 1 ", response.data)
        self.assertIsNone(Country.query.get(1))
