from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
# one way
from wtforms.validators import DataRequired
# another way
from wtforms import validators

class MemberCreateForm(FlaskForm):
    # first arg is name of field in html
    # validators takes an array of validators. You can import a validator specifically
                                            # or call a validator using dot notation
    name = StringField('name', validators=[DataRequired()])
    checked_in = BooleanField('Checked In', validators=[validators.optional()])
