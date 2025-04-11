#Generacion de numeros aleatorios
import random

random_integer = random.randint(1, 20)
print(random_integer)

list_numbers = []
for i in range(20):
   random_integer =  random.randint(1, 20)
   list_numbers.append(random_integer)

print(list_numbers)

random_float = random.random()
print(random_float)
list_floats =  [random.random() for  r in range(10)]
print(list_floats)

import secrets
random_secure = secrets.token_bytes(4)

import uuid
random_uuid = uuid.uuid4()
print(random_uuid)
