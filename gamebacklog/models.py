from gamebacklog import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.genre_name

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(50), unique=True, nullable=False)
    game_description = db.Column(db.Text, nullable=False)