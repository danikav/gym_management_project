from db.run_sql import run_sql
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, class_id) VALUES ( %s, %s ) RETURNING id"
    values = [booking.member.id, booking.gymclass.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gymclass = gymclass_repository.select(row['class_id'])
        booking = Booking(member, gymclass, row['id'])
        bookings.append(booking)
    return bookings

# def delete(id):
#     sql = "DELETE FROM bookings WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)