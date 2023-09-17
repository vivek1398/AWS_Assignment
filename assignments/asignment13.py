								# Assignment #13

'''Write 1 example class for each types of inheritance'''


                                #Single-Level Inheritance
# Parent class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Child class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")
print("!!!Single-Level Inheritnce!!!")
object = Child()
object.func1()
object.func2()

                                # Multiple Inheritance
# Base class1
class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)
# 
# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

print("!!!Multiple Inheritance!!!")
s1 = Son()
s1.fathername = "I AM FATHER CLASS"
s1.mothername = "I AM MOTHER CLASS"
s1.parents()
                                # Multi-Level Inheritance

class Family:
	def show(self):
		print("My Family....") 
class Father(Family):
	name_father = ""
	def show1(self):
	    print(self.name_father) 
class Child(Father):
	name_child = ""
	def show2(self):
		print("Father Name :",self.name_father)
		print("Child Name : ",self.name_child)
		
print("!!!Multi-Level Inheritance!!!")
o = Child()
o.name_father = "I AM FATHER"
o.name_child = "I AM CHILD"
o.show()
o.show2()

                                # Hierarchial Inheritance
class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
		
print("!!!Hierarchial Inheritance!!!")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

                                # Hybrid Inheritance
class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")
print("!!!Hybrid Inheritance!!!")
c = child()