from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gymclass import Gymclass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("classes", __name__)

@gymclasses_blueprint.route("/classes")
def gymclasses():
    gymclasses = gymclass_repository.select_all()
    return render_template("classes/index.html", gymclasses = gymclasses)

@gymclasses_blueprint.route("/classes/new")
def new_class():
    return render_template("classes/new.html")

@gymclasses_blueprint.route("/classes", methods=["POST"])
def create_class():
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    details = request.form["details"]
    new_class = Gymclass(name, date, time, details)
    gymclass_repository.save(new_class)
    return redirect("/classes")

@gymclasses_blueprint.route("/classes/<id>")
def show(id):
    gymclass = gymclass_repository.select_class(id)
    found_members = gymclass_repository.members(gymclass)
    return render_template("classes/show.html", gymclass=gymclass, members=found_members)

@gymclasses_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    gymclass = gymclass_repository.select_class(id)
    return render_template('classes/edit.html', gymclass=gymclass)


@gymclasses_blueprint.route("/classes/<id>", methods=["POST"])
def update_class(id):
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    details = request.form["details"]
    gymclass = Gymclass(name, date, time, details, id)
    gymclass_repository.update(gymclass)
    return redirect("/classes")