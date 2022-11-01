from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class NameSubmit(FlaskForm):
    input_name = StringField("Name", validators=[DataRequired()])
