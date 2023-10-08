from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL, Optional, NumberRange, AnyOf

class CupcakeForm(FlaskForm):
    """Form for adding a pet"""
    flavor = StringField("Flavor", 
                       validators=[DataRequired()])
    size = SelectField("Size", choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')],
                          validators=[DataRequired(), AnyOf(values=['small', 'medium', 'large'])])
    image = StringField("Image URL",
                            validators=[Optional(), URL()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=0, max=10, message='Enter a rating between 0 and 30')])