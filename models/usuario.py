from db import db
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    genero = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)