from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    pflegeplaene = db.relationship('Pflegeplan', backref='author', lazy='dynamic')

    def set_password(self, password):
        """
        Sets the user's password hash.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks the user's password against the stored hash.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Pflegeplan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientenname = db.Column(db.String(64), nullable=False)
    informationen = db.Column(db.Text)
    probleme_ressourcen = db.Column(db.Text)
    pflegeziele = db.Column(db.Text)
    pflegemassnahmen = db.Column(db.Text)
    durchfuehrung = db.Column(db.Text)
    beurteilung = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pflegeberichte = db.relationship('Pflegebericht', backref='pflegeplan', lazy='dynamic')

    def __repr__(self):
        return f'<Pflegeplan {self.patientenname}>'

    def to_dict(self):
        return {
            'id': self.id,
            'patientenname': self.patientenname,
            'informationen': self.informationen,
            'probleme_ressourcen': self.probleme_ressourcen,
            'pflegeziele': self.pflegeziele,
            'pflegemassnahmen': self.pflegemassnahmen,
            'durchfuehrung': self.durchfuehrung,
            'beurteilung': self.beurteilung,
            'timestamp': self.timestamp,
            'user_id': self.user_id
        }

class Pflegebericht(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    inhalt = db.Column(db.Text, nullable=False)
    pflegeplan_id = db.Column(db.Integer, db.ForeignKey('pflegeplan.id'), nullable=False)

    def __repr__(self):
        return f'<Pflegebericht {self.inhalt[:20]}>'

    def to_dict(self):
        return {
            'id': self.id,
            'datum': self.datum,
            'inhalt': self.inhalt,
            'pflegeplan_id': self.pflegeplan_id
        }
