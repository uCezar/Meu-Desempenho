import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-local")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///meu_desempenho.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
