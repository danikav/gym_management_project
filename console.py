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

gymclass1 = Gymclass('Zumba', '02/04/21', '19:00', 'Exercise and dance and have fun!')
gymclass_repository.save(gymclass1)

gymclass2 = Gymclass('Kickboxing', '04/04/21', '21:00', 'Get fit and seek vengeance on your enemies')
gymclass_repository.save(gymclass2)

gymclass3 = Gymclass('Aikido', '06/04/21', '17:00', 'Learn about the magical powers of stillness and spoons')
gymclass_repository.save(gymclass3)

pdb.set_trace()