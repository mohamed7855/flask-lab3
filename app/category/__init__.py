
from flask import Blueprint

category_blueprint = Blueprint("categories", __name__, url_prefix="/categories")

from app.category import views