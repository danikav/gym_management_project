from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gymclass import Gymclass
from models.booking import Booking
import repositories.gymclass_repository as gymclass_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository

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
    capacity = request.form['capacity']
    details = request.form["details"]
    peak = request.form["peak"]
    new_class = Gymclass(name, date, time, capacity, details, peak)
    gymclass_repository.save(new_class)
    return redirect("/classes")

@gymclasses_blueprint.route("/classes/<id>/bookings")
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
    capacity = request.form["capacity"]
    details = request.form["details"]
    peak = request.form["peak"]
    gymclass = Gymclass(name, date, time, capacity, details, peak, id)
    gymclass_repository.update(gymclass)
    return redirect("/classes")

@gymclasses_blueprint.route("/classes/<id>/book")
def book_member(id):
    gymclass = gymclass_repository.select_class(id)
    already_booked_members = gymclass_repository.members(gymclass)

    already_booked_member_ids = [member.id for member in already_booked_members]

    if gymclass.peak:
        members = member_repository.select_premium()
    else:
        members = member_repository.select_all()
    return render_template('classes/book.html', gymclass=gymclass, members=members, already_booked_member_ids=already_booked_member_ids)

@gymclasses_blueprint.route("/classes/<id>/bookings", methods=["POST"])
def update_bookings(id):
    member_id = request.form["membername"]
    member = member_repository.select_member(member_id)
    gymclass = gymclass_repository.select_class(id)
    booking = Booking(member, gymclass, id)

    members = gymclass_repository.members(gymclass)
    if len(members) < gymclass.capacity:
        booking_repository.save(booking)
    else:
        return render_template('classes/full.html')
    return redirect(f"/classes/{id}/bookings")