from db.run_sql import run_sql
from models.member import Member
from models.gymclass import Gymclass

def save(member):
    sql = "INSERT INTO members( name, membertype ) VALUES ( %s, %s ) RETURNING id"
    values = [member.name, member.membertype]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['membertype'], row['id'])
        members.append(member)
    return members

def select_member(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['membertype'], result['id'] )
    return member

def update(member):
    sql = "UPDATE members SET (name, membertype) = (%s, %s) WHERE id = %s"
    values = [member.name, member.membertype, member.id]
    run_sql(sql, values)

def classes(member):
    values = [member.id]
    sql = """
        SELECT classes.* FROM classes
        INNER JOIN bookings
        ON classes.id = bookings.class_id
        WHERE member_id = %s
    """

    results = run_sql(sql, values)
    gymclasses = []

    for row in results:
        gymclass = Gymclass(row["name"], row["date"], row["time"], row["capacity"], row["details"], row["peak"], row["id"])
        gymclasses.append(gymclass)
        
    return gymclasses

def select_premium():
    members = []

    sql = "SELECT * FROM members WHERE membertype = 'premium'"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['membertype'], row['id'])
        members.append(member)
    return members

# def delete(id):
#     sql = "DELETE FROM members WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)