#----------------------------------------OOP----------------------------------------------------------------

# Syntax
# class class'anme:
#     Constructor of class

#     def __init__(self, other_data)
#         self.Attribute = parameter
#         self.Attribute = parameter                => form of create class
#         self.Attribute = parameter

#     def func'name (self)
#       self.constructer

# Var'name = class'name(parameter, ...)             => create new Instance
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# @classmethod
# def Func'name(cls)                        => to create class Method
#    cls.constructer
#                                                                       => In Constructor of class
# @staticmethod
# def Func'name(parameter[opt])             => to create static Method
#    constructer
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Magic Method
# __init__                                                              => Called Automatically When Instantiating Class

# self.__                                                               => class__ The class to which a class instance belongs

# __str__                                                               => Gives a Human-Readable Output of the Object

# __len__                                                               => Returns the Length of the Container
#                                                                               Called When We Use the Built-in len() Function on the Object


#Inheritance
# class'name(inherited class'name)                                      => to inherit method from class
#       def__init__(self, other_data)
#            
#               inherited class'name.__init__(self, other_data)         => to inherit Atteribute instance from Class,
                # OR
#               super().__init__(other_data)                                    All Atter instance in the main class must be written


# class'name(inherited class'name, inherited class'name, ...)           => to multi inherit method from 



# @property
# def func'name(self):
#   return                                                              => to convert function not accept param but (self) to property
#
# print(func'name)



# Class Called Abstract Class If it Has One or More Abstract Methods
# abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# By Adding @absttractmethod Decorator on The Methods
# ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

# from abc import ABCMeta, abstractmethod
# class class'name(metaclass=ABCMeta):
#                                                                       => form of abstract Function
#     @abstractmethod
#     def func'name(self):
#         pass

####################################  EXAMPLE  #################################################################

# class cars:
#     CountOfCars = 0
#     def __init__(self, Name, Model):
#         self.name_car = Name
#         self.model_car = Model
#         cars.CountOfCars += 1
    
#     def delet_car(self):
#         cars.CountOfCars -= 1
#         return "car is deleted"

# print(cars.CountOfCars)
# Fcar = cars("Nassen", 2019)
# Scar = cars("BMW", 2020)
# Scar = cars("Toyota", 2015)
# Scar = cars("4X4", 2021)
# print(cars.CountOfCars)

# print(Fcar.delet_car())
# print(cars.CountOfCars)

# print(Fcar.name_car, Fcar.model_car)
# print(Scar.name_car, Scar.model_car)


#--------------------------------------------------------------------------------------------------------


# class Member :
#     user = 0
#     invaild_country = "Israel"

#     @classmethod
#     def count_user(cls):
#         print(f"count of user '{cls.user}'")

#     @staticmethod
#     def say_welcome():
#         print(" WELCOME IN OUR CLUB ".center(40, "#"))
        
#     def __init__(self, Fname, Mname, Lname, gender, country):
#         self.first_name   = Fname 
#         self.middle_name  = Mname 
#         self.last_name    = Lname 
#         self.your_gender  = gender
#         self.your_country = country
        
#         Member.user +=1
        
#     def hello (self):
#         if self.your_gender == "male":
#             return f"hello Mr {self.first_name}"

#         elif self.your_gender == "female":
#             return f"hello Miss: {self.first_name}"

#     def Full_name(self):
#             return f"Your Full Name: {self.first_name} {self.middle_name} {self.last_name}"

#     def leave(self):
#         if self.your_country == Member.invaild_country:
#             raise ValueError (f"this country '{self.your_country}' not exist")
#         else:
#             return f"welcom from {self.your_country}"

#     def info(self):
#         return f"{self.hello()}\n{self.Full_name()}\n{self.leave()}"

# Member.say_welcome()
# print()

# mem_one = Member("Abdo", "Hamdy", "Elgendy", "male", "Egypt")
# mem_tow = Member("Ahmed", "Hamdy", "Elgendy", "male", "Egypt")
# mem_three = Member("Mohamed", "Hamdy", "Elgendy", "male", "Egypt")

# print(mem_one.info())
# print()
# print(mem_tow.info())
# print()
# print(mem_three.info())

# print("*" * 20)

# Member.count_user()


#--------------------------------------------------------------------------------------------------------


# class skill:

#     def __init__(self) :
#         self.skills = ["Html", "Js", "Py"]

#     def __str__(self) -> str:
#         return "return a Human-Readable Output of the Object"

#     def __len__(self):
#         return len(self.skills)

# print(str().__class__)

# print(skill().__class__)

# print(skill())

# mustVar = skill()
# mustVar.skills.append("DOM")
# mustVar.skills.append("BOM")

# print(len(mustVar))

# for magic in dir(skill()):
#     print(magic)



#ineritance
# class order:
#     menu_eat = {"rise": 15,
#             "fish": 45,
#             "chicken":70,
#             "meet": 100}

#     menu_drinks = {"mango": 15,
#             "watermilon": 10,
#             "Strawberry":20,
#             "Guava": 15}

#     def __init__(self, name, amount):
#         self.name = name
#         self.amout = amount


# class eat(order):
#     def __init__(self, name, amount):
#         super().__init__(name, amount)

#         if name in order.menu_eat :
#             print(f"You order '{self.amout}' amount of '{self.name}' And all price = {order.menu_eat[self.name] * amount}.LE")
#         else:
#             print("meal exist Menu")

# class drink(order):
#     def __init__(self, name, amount):
#         super().__init__(name, amount)

#         if name in order.menu_drinks:
#             print(f"You order '{self.amout}' amount of '{self.name}' juice And all price = {order.menu_drinks[self.name] * amount}.LE")

#         else:
#             print("drink exist Menu")

# cus1 = eat("rise", 2)
# cus1 = drink("Guava", 2)


# class person:
#     def __init__(self, name, address):
#         self.his_name = name
#         self.his_address = address

#     def say_hello(self):
#         return f"Hello {self.his_name}, Are You From {self.his_address}"

#     def say_welcome(self):
#         print(f"Hello {self.his_name}")
#         raise NotImplementedError("this function must implement")


# class student(person):
#     def __init__(self, name, address):
#         # person.__init__(self, name, address)
#         super().__init__(name, address)

#         # self.his_name = name
#         # self.his_address = address

#     def say_hello(self):
#         return f"Hello stu: {self.his_name}, Are You From {self.his_address}"

#     # def say_hello(self):
#     #     return f"Hello {self.his_name}, Are You From {self.his_address}"


# class teacher(student, person):
#     def __init__(self, name, address):
#         super().__init__(name, address)  

#     def say_hello(self):
#         return f"Hello master: {self.his_name}, Are You From {self.his_address}"

# stu1 = student("Ahmed", "fayoum")
# teach1 = teacher("Moamed", "Nasr city")

# print(stu1.say_hello())
# print(teach1.say_hello())


# print(stu1.say_welcome())

# class A:
#         def doSome(self) -> None:
#             print("WELLCOME")
#             raise NotImplementedError("this function must implement")

# class B(A):
#         def doSome(self) -> None:
#             print("WELLCOME")


# var1 = B().doSome()
# var1 = B("abdo").doSome()



#Encapsulation
# class Encapsulation:
#     def __init__(self, name):
        # self.name  = name     # puplic
        # self._name  = name    # proteceted
#         self.__name  = name   # private 

# var1 = Encapsulation("ahmed")
# print(var1._Encapsulation__name)

# # var1._Encapsulation__name = "abdo"
# # print(var1._Encapsulation__name)



#Seter And Geter
# class C:
#     def __init__(self, name) -> None:
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self, NewName):
#         self.__name = NewName

# var1 = C("Abdo")
# print(var1.get_name())

# var1.set_name("Ahmed")
# print(var1.get_name())



# class property:
#     def __init__(self, name):
#         self.name = name
#     @property
#     def say_hello(self):
#         return f"hello {self.name}"

# var1 = property("abdo")

# print(var1.say_hello)

# from abc import ABCMeta, abstractmethod

# class status(metaclass=ABCMeta):
    
#     @abstractmethod
#     def happy(self):
#         pass

# class son(status):
#     def happy(self):
#         return "yes"

# class daughter(status):
#     def happy(self):
#         return "No"

# var1 = status().happy() # Can't instantiate abstract class status with abstract method happy
# print(var1)

# var1 = son().happy()
# print(var1)

# var1 = daughter().happy()
# print(var1)

