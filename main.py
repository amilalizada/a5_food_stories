# class Human:
#     age = 20

#     def __init__(self, name, surname) -> None:
#         self.name = name
#         self.surname = surname

#     def get_fullname(self):
#         return self.name + ' ' + self.surname
    
#     def get_age(self):
#         return self.age
    
#     def __str__(self) -> str:
#         return self.name
    
#     def call(self):
#         fullname = self.get_fullname()
#         if fullname:
#             print("ok")
#         else:
#             return None

#         age = self.get_age()

#         return f'{fullname} is {age} years old'
    
# class A:
#     def get_fullname(self):
#         return 'Other Name'
    
# class B:
#     def get_fullname(self):
#         return 'Abdulla'
    
# class Person(Human, A, B):
#     def get_fullname(self):
#         return super(A, self).get_fullname() + ' Jr.'

# obj = Person('John', 'Doe')
# print(obj.get_fullname())


# class Human:
#     __age = 20
#     _height = 180
#     def __init__(self, name, surname) -> None:
#         self.name = name
#         self.surname = surname

#     def get_fullname(self):
#         return self.name + ' ' + self.surname
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Age must be an integer')
#         self.__age = value
    
#     def __str__(self) -> str:
#         return self.name
    
#     def call(self):
#         fullname = self.get_fullname()
#         if fullname:
#             print("ok")
#         else:
#             return None

#         age = self.get_age()

#         return f'{fullname} is {age} years old'
    
# obj = Human('John', 'Doe')
# print(obj.age)
# obj.age = 25
# print(obj.age)
# print(obj._height)
from abc import ABC, abstractmethod
import json

my_dict = {
    "name": "John",
    "surname": "Doe",
    "age": 30
}

dict_str = json.dumps(my_dict)
# print(dict_str, type(dict_str))
# for i in dict_str:
#     print(i)

reverse_dict = json.loads(dict_str)
print(reverse_dict, type(reverse_dict))

for k, v in reverse_dict.items():
    print(v)


# class Vehicle(ABC):
#     def start(self):
#         print("started")
#     @abstractmethod 
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def stop(self):
#         ...
#     def voice(self):
#         print("Vroom")

# car_obj = Car()
# car_obj.start()











