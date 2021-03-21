from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
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
        member = Member(row['name'], row['id'])
        members.append(member)
    return members