from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CountryForm(FlaskForm):
    description = StringField("Country Name", validators = [DataRequired()])
    submit = SubmitField("Add Country")