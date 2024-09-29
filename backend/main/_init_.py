# backend/pflege-app/main/__init__.py
from flask import Blueprint

bp = Blueprint('main', __name__)

from backend import routes  # Importiere die Routen, um sie zu registrieren

