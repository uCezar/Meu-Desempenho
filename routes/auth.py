from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import func
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    return render_template("cadastro.html")

  

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")