from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from sqlalchemy import func

class User(db.Model):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def set_password(self, password):
        """Set password for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored password hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Pflegeplan(db.Model):
    """Pflegeplan model for storing care plan details."""
    id = db.Column(db.Integer, primary_key=True)
    patientenname = db.Column(db.String(120), nullable=False)
    informationen = db.Column(db.Text, nullable=True)
    probleme_ressourcen = db.Column(db.Text, nullable=True)
    pflegeziele = db.Column(db.Text, nullable=True)
    pflegemassnahmen = db.Column(db.Text, nullable=True)
    durchfuehrung = db.Column(db.Text, nullable=True)
    beurteilung = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('pflegeplaene', lazy=True))

    def __repr__(self):
        return f'<Pflegeplan {self.patientenname}>'

    def to_dict(self):
        """Convert Pflegeplan instance to dictionary."""
        return {
            'id': self.id,
            'patientenname': self.patientenname,
            'informationen': self.informationen,
            'probleme_ressourcen': self.probleme_ressourcen,
            'pflegeziele': self.pflegeziele,
            'pflegemassnahmen': self.pflegemassnahmen,
            'durchfuehrung': self.durchfuehrung,
            'beurteilung': self.beurteilung,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'user_id': self.user_id
        }

class Pflegebericht(db.Model):
    """Pflegebericht model for storing care report details."""
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.DateTime, nullable=False, default=func.now())
    inhalt = db.Column(db.Text, nullable=False)
    pflegeplan_id = db.Column(db.Integer, db.ForeignKey('pflegeplan.id'), nullable=False)
    pflegeplan = db.relationship('Pflegeplan', backref=db.backref('pflegeberichte', lazy=True))

    def __repr__(self):
        return f'<Pflegebericht {self.id} für Pflegeplan {self.pflegeplan_id}>'