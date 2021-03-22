from db.run_sql import run_sql
from models.gymclass import Gymclass

def save(gymclass):
    sql = "INSERT INTO classes( name, date, time, details ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.time, gymclass.details]
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
        gymclass = Gymclass(row['name'], row['date'], row['time'], row['details'] )
        gymclasses.append(gymclass)
    return gymclasses

def select_class(id):
    gymclass = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gymclass = Gymclass(result['name'], result['date'], result['time'], result['details'] )
    return gymclass