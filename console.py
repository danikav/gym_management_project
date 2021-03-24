import pdb
from models.member import Member
from models.gymclass import Gymclass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
gymclass_repository.delete_all()


member1 = Member('Othniel Adalwolf', 'premium')
member_repository.save(member1)

member2 = Member('Sylvaine Marilyn', 'standard')
member_repository.save(member2)

member3 = Member('Francisca Maia', 'standard')
member_repository.save(member3)

member4 = Member('Maria Chiara Zavier', 'premium')
member_repository.save(member4)

member5 = Member('Evpraksiya Jani', 'standard')
member_repository.save(member5)

member6 = Member('Chris Beless', 'premium')
member_repository.save(member6)

member7 = Member('Mila Cerveira', 'standard')
member_repository.save(member7)

member8 = Member('Dani Kavanagh', 'premium')
member_repository.save(member8)

gymclass1 = Gymclass('Zumba', '02/04/21', '19:00', 5, 'Exercise and dance and have fun!', False)
gymclass_repository.save(gymclass1)

gymclass2 = Gymclass('Kickboxing', '04/04/21', '21:00', 8, 'Get fit and seek vengeance on your enemies', True)
gymclass_repository.save(gymclass2)

gymclass3 = Gymclass('Aikido', '06/04/21', '17:00', 10,  'Learn about the magical powers of stillness and spoons', False)
gymclass_repository.save(gymclass3)

booking1 = Booking(member1, gymclass1)
booking_repository.save(booking1)

booking2 = Booking(member3, gymclass2)
booking_repository.save(booking2)


pdb.set_trace()