# class Person:
#     human = True
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     @property
#     def greet(self):
#         print(f"Hello, my name is {self.name}")

#     def full_name(self):
#         return f"{self.name} {self.surname}"
    
#     @classmethod
#     def divide_fullname(cls, fullname, age):
#         name, surname = fullname.split(" ")
#         return cls(name, surname, age)
    
#     @classmethod
#     def change_human(cls, new_value):
#         cls.human = new_value

#     @staticmethod
#     def is_adult(age):
#         return age > 18
    


# obj = Person("John", "Doe", 20)
# obj.greet




