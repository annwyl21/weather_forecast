from wtforms import SelectField, SubmitField
from flask_wtf import FlaskForm

class LocationForm(FlaskForm):
    location = SelectField('Location', choices=[('london', 'London'), ('oxford', 'Oxford'), ('cambridge', 'Cambridge')])
    submit = SubmitField('Submit')
    