import pdb
from models.member import Member

import repositories.member_repository as member_repository

member_repository.delete_all()

member1 = Member('Othniel Adalwolf')
member_repository.save(member1)

member2 = Member('Sylvaine Marilyn')
member_repository.save(member2)

member3 = Member('Francisca Maia')
member_repository.save(member3)

member4 = Member('Maria Chiara Zavier')
member_repository.save(member4)

member5 = Member('Evpraksiya Jani')
member_repository.save(member5)

pdb.set_trace()