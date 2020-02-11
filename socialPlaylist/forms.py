from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from socialPlaylist.models import User

class RegForm(FlaskForm):
    # These variable names must be used in the html
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    accept_tos = BooleanField('I accept the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    # Pass username form field (defined above, but can be named anything below)
    # Validation methods must follow the validate_<field_name> convention
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # Find first instance of user with this username
        if user:
            raise ValidationError('That username is taken.')

    # Pass email form field (defined above, but can be named anything below)
    # Validation methods must follow the validate_<field_name> convention
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()  # Find first instance of user with this email
        if user:
            raise ValidationError('That email is taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CreatePlaylistForm(FlaskForm):
    playlist_name = StringField('Playlist Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class AddSongForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    artist_firstname = StringField('Artist First Name', validators=[DataRequired()])
    artist_lastname = StringField('Artist Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')