from db.run_sql import run_sql
from models.gymclass import Gymclass
from models.member import Member

def save(gymclass):
    sql = "INSERT INTO classes( name, date, time, capacity, details, peak ) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.time, gymclass.capacity, gymclass.details, gymclass.peak]
    results = run_sql( sql, values )
    gymclass.id = results[0]['id']
    return gymclass

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

def select_all():
    gymclasses = []

    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for row in results:
        gymclass = Gymclass(row['name'], row['date'], row['time'], row['capacity'], row['details'], row['peak'], row['id'] )
        gymclasses.append(gymclass)
    return gymclasses

def select_class(id):
    gymclass = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gymclass = Gymclass(result['name'], result['date'], result['time'], result['capacity'], result['details'], result['peak'], result['id'] )
    return gymclass

def update(gymclass):
    sql = "UPDATE classes SET (name, date, time, capacity, details, peak) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gymclass.name, gymclass.date, gymclass.time, gymclass.capacity, gymclass.details, gymclass.peak, gymclass.id]
    run_sql(sql, values)
    
def members(gymclass):
    values = [gymclass.id]
    sql = """
        SELECT members.* FROM members
        INNER JOIN bookings
        ON members.id = bookings.member_id
        WHERE class_id = %s
    """

    results = run_sql(sql, values)
    members = []

    for row in results:
        member = Member(row["name"], row["id"])
        members.append(member)
        
    return members