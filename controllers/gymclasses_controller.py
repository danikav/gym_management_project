from flask import Flask, render_template
from flask import Blueprint
from models.gymclass import Gymclass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("classes", __name__)

@gymclasses_blueprint.route("/classes")
def gymclasses():
    gymclasses = gymclass_repository.select_all()
    return render_template("classes/index.html", gymclasses = gymclasses)