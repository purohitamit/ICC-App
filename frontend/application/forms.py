from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CountryForm(FlaskForm):
    country_name = StringField("Country Name", validators = [DataRequired()])
    submit = SubmitField("Add Country")

class PlayerForm(FlaskForm):
    player_name = StringField("Player Name", validators = [DataRequired()])
    team = SelectField("Team", choices=[])
    submit = SubmitField("Add Player")
