from gamebacklog import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(25), unique=True, nullable=False)
    games = db.relationship("Game", backref="genre", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.genre_name

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(50), unique=True, nullable=False)
    game_description = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Game: {1} | Release: {2}".format(
            self.id, self.game_name, self.release_date
        )