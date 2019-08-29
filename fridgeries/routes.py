from flask import render_template, url_for, flash, redirect, request
from fridgeries import app, db, login_manager
from flask_login import login_user, current_user, logout_user, login_required
from fridgeries.models import Korisnik, Namirnice
import sqlite3

@app.route('/')
def show():
   return redirect(url_for('showprijava'))
@app.route('/prijava', methods=['GET','POST'])
def showprijava():
	if current_user.is_authenticated:
		return redirect(url_for('shownaslovna'))
	if request.method == 'POST':
		if request.form.get('prij'):
			email = request.form.get('email')
			lozinka = request.form.get('lozinka')
			korisnik = Korisnik.query.filter_by(email_korisnika = email, lozinka_korisnika = lozinka).first()		
			if korisnik is None:
				flash("Korisnik ne postoji")
				return render_template('prijava.html')
			else:
				login_user(korisnik)
				return redirect(url_for('shownaslovna'))
					
		
	return render_template('prijava.html')
	
@app.route('/odjava')
def odjava():
	logout_user()
	return redirect(url_for('showprijava'))
	
	
@app.route('/registracija', methods=['POST','GET'])
def showregistracija():
	if request.method == 'POST':
		if request.form.get('reg'):
			ime = request.form.get('ime')
			prezime = request.form.get('prezime')
			email = request.form.get('email')
			lozinka = request.form.get('lozinka')
			korisnik = Korisnik.query.filter_by(email_korisnika = email).first()
			if korisnik is None:
				korisnik = Korisnik(ime_korisnika = ime, prezime_korisnika = prezime, email_korisnika=email , lozinka_korisnika = lozinka)
				db.session.add(korisnik)
				db.session.commit()
				flash("Uspjesno ste se registrirali, prijavite se!")
				return redirect(url_for('showprijava'))
			else:
				flash("Korisnik već postoji")
				return render_template('registracija.html')
			

	return render_template('registracija.html')	
	
@app.route('/naslovna', methods=['POST','GET'])
@login_required
def shownaslovna():	
	if request.method == 'POST':
		if request.form.get('prikaz'): 
			result = Namirnice.query.filter_by(korisnik_id = current_user.id).all()
			if result == []:
				print("prazno")	
				return redirect(url_for('showunos'))						
			else:					
				return render_template("naslovna.html", result=result)	
			
	if request.method == 'POST':
		if request.form.get('obr'):		
			naziv = request.form.get('naziv')			
			namirnice = Namirnice.query.filter_by(ime_namirnice = naziv).first()
			print (namirnice)
			if namirnice is None:
				return render_template("naslovna.html")
			else:
				db.session.delete(namirnice)
				db.session.commit()
			
	return render_template("naslovna.html")
    


@app.route('/unos', methods=['GET','POST'])
@login_required
def showunos():
	if request.method == 'POST':
		if request.form.get('unos'):
			imenamirnice = request.form.get ('imenamirnice')
			kategorija = request.form.get('kategorija')
			namirnice = Namirnice(ime_namirnice = imenamirnice, kategorija_namirnice = kategorija, autor = current_user)
			db.session.add(namirnice)
			db.session.commit()


	return render_template("unos.html")
    	
    