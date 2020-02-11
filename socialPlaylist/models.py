from socialPlaylist import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 


class Playlists(db.Model):
    __tablename__ = 'Playlists'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), foreign_key=True) 
    playlist_name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Playlist {}>'.format(self.playlist_name)

