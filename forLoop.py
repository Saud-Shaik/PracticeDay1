languages=["python","java","swift","C","C++"]
for language in languages:
   if language=="swift" or language=="C++":
    continue
   print(language)

text="python"
for character in text:
     print(character)

#python range()

for count in range(1,6):
    print(count)

number=int(input("Enter a number: 5"))
for count in range(1,11):
    product=number*count
    
    print(number,"x",count,"=",product)

#can you create a program to find the sum of numbers from 1 to 100
#the result should be equal to 1+2+3+...+100
total=0
for number in range(1,101):
    total=total+number
    print(total)

#break and continue

for item in range(1,6):
    if item==3:
        break
    
    print(item)

for i in range(5):
    number=float(input("Enter a number"))
    if number<0:
        continue
    print(number)

#Functions
def greet():
    print("Hello")

greet()

#pyhton arguments
def greet(name):
    print("Hello",name)
greet("saud")

def add_numbers(n1,n2):
    result=n1+n2
    print("the sum is",result)
add_numbers(4.5,4.5)

def add_numbers(n1,n2):
    result=n1+n2
    return result
finalResult=add_numbers(4.5,6)
print("the sum is",finalResult)

#functions to find average marks
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects

    return average_marks
#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks>=80:
        grade="A"
    elif average_marks >=60:
        grade="B"
    elif average_marks >=50:
        grade="C"
    else:
        grade="F"
    return grade
marks=[85,90,75,80,90]
final_average_mark=find_average_marks(marks)
print("Your average mark is :",final_average_mark)
final_grade=compute_grade(final_average_mark)
print("Your grade is:",final_grade)

#List and Tuples
languages=["Python","Java","C++","Kotlin"]
languages[1]="Ruby"
print(languages)
#List Methods

languages.append("Rust")
print(languages)
languages.insert(2,"JS")
print(languages)
languages.remove("C++")
print(languages)
language1=languages.copy
print(language1)
