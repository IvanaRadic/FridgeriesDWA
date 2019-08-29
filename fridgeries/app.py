from flask import Flask,render_template,request,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt
from fridgeries.views.index import bp as index_bp
from fridgeries.views.registracija import bp as registracija_bp
from fridgeries.views.prijava import bp as prijava_bp
from fridgeries.views.naslovna import bp as naslovna_bp
from fridgeries.views.unos import bp as unos_bp
import sqlite3


app = Flask(__name__)


app.register_blueprint(index_bp)
app.register_blueprint(registracija_bp)
app.register_blueprint(prijava_bp)
app.register_blueprint(naslovna_bp)
app.register_blueprint(unos_bp)

app.secret_key="mau789"
