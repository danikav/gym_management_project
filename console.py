import pdb
from models.member import Member
from models.gymclass import Gymclass

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

member_repository.delete_all()
gymclass_repository.delete_all()

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

gymclass1 = Gymclass('Zumba', '12/03/21', '19:00', 'Exercise and dance and have fun!')

pdb.set_trace()