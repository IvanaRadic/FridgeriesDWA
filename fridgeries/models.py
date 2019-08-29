from fridgeries import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_korisnik(korisnik_id):
	return Korisnik.query.get(int(korisnik_id))

class Korisnik(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	ime_korisnika = db.Column(db.String(20), unique=True, nullable=False)
	prezime_korisnika = db.Column(db.String(20), unique=True, nullable=False)
	email_korisnika = db.Column(db.String(120), unique=True, nullable=False)
	lozinka_korisnika = db.Column(db.String(60), nullable=False)
	namirnice = db.relationship('Namirnice', backref='autor', lazy=True)
	def __repr__(self):
		return f"Korisnik('{self.ime_korisnika}','{prezime_korisnika}', '{self.email_korisnika}')"

class Namirnice(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ime_namirnice = db.Column(db.String(20), nullable=False)
	kategorija_namirnice = db.Column(db.String(20), nullable=False)
	korisnik_id = db.Column(db.Integer, db.ForeignKey('korisnik.id'), nullable=False)
	def __repr__(self):
		return f"Korisnik('{self.ime_namirnice}','{self.kategorija_namirnice}')"		