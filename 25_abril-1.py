import datetime
# modelos de datos
# mcd modelo vista controlador
# clase usuario User id_nif, birhtday, email, phone, password

class User: 
    
# constructor, metodo especial que permite crear objetos
def__init__(self, id, nif, birthday, email, phone, password = "admin"):
    self.id = id
    self.nif = nif
    self.birthday = birthday
    self.email = email
    self.phone = phone
    self.password = password
    
    
    user1 = user(1, '77788887', datetime.date(1995, 1, 1), 'user1@gmail.com', '91333455')
    user2 = user(2, '8884e848', datetime.date.fromisoformat("1998-2-25"), 'user2@gmail.com', '5555555')
    
    print (user1.birthday)
    print (user2.birthday)

# clase direccion Adress: calle, city, postal_code, country

import datetime

def__init__(self, calle, city, postal_code, country):
    self.calle = calle 
    self.city = city
    self.postal_code = postal_code
    self.country = country
    
    
user1 = user(1, 'primo de rivera', 'madrid', 28032, 'espana')
user2 = user(2, 'avenida de america', 'madrid', 28012, 'espana')

print(user2.calle)
print(user2.calle)



# asociados


