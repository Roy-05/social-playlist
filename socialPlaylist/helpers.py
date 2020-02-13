from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user
from socialPlaylist.models import User, Playlists
from socialPlaylist import db

def submitLogin(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    login_user(user)
    #flash('Logged In!', 'success')
    return redirect(url_for('playlist'))


def showLoginForm(form):
    return render_template('login.html', title='Login', form=form)

def getPlaylists():
    return Playlists.query.filter_by(username=current_user.username)

def addNewPlaylist(form):
    if form.validate_on_submit():
        playlist = Playlists(
                    username = current_user.username,
                    playlist_name = form.playlist_name.data,
                    user_id = current_user.id
                    )
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('playlist'))