from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#DB기본 코드----------------------------------------------------


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.username} {self.title} 추천 by {self.username}'

with app.app_context():
    db.create_all()
#-----------------------------------------------------------------

@app.route("/")
def home():
    name = '전민성'
    motto = "행복해서 웃는게 아니라 웃어서 행복합니다."

    context = {
        "name": name,
        "motto": motto,
    }
    return render_template('motto.html', data=context)

@app.route("/music/")
def music():
    song_list = Song.query.all()
    return render_template('music.html', data = song_list)

# @app.route("/music/<username>")
# def render_music_filter(username):
#     filter_list = Song.query.filter_by(username=username).all()
#     return render_template('music.html', data = filter_list)


@app.route("/music/create/")
def music_create():
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_receive = request.args.get("image_url")
    print(title_receive)
    song = Song(username = username_receive, title = title_receive, artist = artist_receive, image_url = image_receive)
    print(song)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('music'))

@app.route("/music/change/")
def music_change():
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_receive = request.args.get("image_url")
    id_receive = request.args.get("id")
    
    song_data = Song.query.filter_by(id=id_receive).first()
    song_data.title = title_receive
    song_data.artist = artist_receive
    song_data.username = username_receive
    song_data.image_url = image_receive
    db.session.commit()
    return redirect(url_for('music'))

if __name__ == "__main__":
    app.run(debug=True)