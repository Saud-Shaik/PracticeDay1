#Object oriented Programming

class Student:
    pass
student1=Student()
student1.name="Saud"
student1.marks=85
print(student1.name)
print(student1.marks)

#function in class

class Students:
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False

student2=Students()
student2.marks=85
student2.name="Saud"
did_pass=student2.check_pass_fail()
print(did_pass)

class StudentDetails:
 def __init__(self,name,marks):
    self.name=name
    self.marks=marks

studentDetails=StudentDetails("Harry",79)
print(studentDetails.name)
print(studentDetails.marks)

#Add two complex numbers

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,number):
        real=self.real+number.real
        imag=self.imag+number.imag
        result=complex(real,imag)
        return result
n1=Complex(5,6)
n2=Complex(-4,2)
result=n1.add(n2)
print("real",result.real)
print("imag=",result.imag)

#Inheritance

class Animals:
    def eat(self):
        print("I can eat")
class Dog(Animals):
    def bark(self):
        print("I can bark")
class Cat(Dog):
    def meow(self):
        print("Ican meow")
dog1=Dog()
dog1.bark()
dog1.eat()
cat1=Cat()
cat1.bark()

class Polygon:
    def __init__(self,sides):
        self.sides=sides
    def display_info(self):
        print("A polygon is a two dimensional shape with straight line")
    def get_perimeter(self):
        perimeter=sum(self.sides)
        return perimeter
class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self)
class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
t1=Triangle([5,6,7])
perimeter=t1.get_perimeter()
t1.display_info()
print("The perimeter is",perimeter)


#Try catch finally

try:
    numarators=int(input("Enter numerators:")) 
    denominator=int(input("Enter denominator:"))
    result=numarators/denominator
    print(result)
except:
       print("Denominator can not be 0,please try again")
print("Program ends")

try:
    print(1/0)
except:
    print("wrong denominator")
finally:
    print("Always printed")


