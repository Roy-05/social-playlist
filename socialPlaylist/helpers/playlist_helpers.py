from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user
from socialPlaylist.models import User, Playlists
from socialPlaylist import db


def get_playlists():
    return Playlists.query.filter_by(username=current_user.username)


def add_new_playlist(form):
    if form.validate_on_submit():
        playlist = Playlists(
            username=current_user.username,
            playlist_name=form.playlist_name.data,
            user_id=current_user.id
        )
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('playlist'))
