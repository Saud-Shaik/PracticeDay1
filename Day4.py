#tuple
numbers=(21,-5,6,9)
print(numbers)
for number in numbers:
    print(number)

#String operation
text1="python"
text2="programming"
result=text1+" "+text2
new_text=text1*3
print(result)
print(new_text)
for char in text1:
    print(char)
print(len(text1))

#String methods

text="I Like Python 3"
result=text.lower()
result1=text.upper()
result2=text.find("Python")
result3=text.replace("Python 3","Java")
print(result)
print(result1)
print(result2)
print(result3)

#output
quote="Talk cheap. show me the code"
print("1.",quote[5])
print("2.",quote[-3])
print("3.",quote.replace("code","programming"))

#Dictionaries to store key/value pair

person1={"name":"saud","age":25}
print(person1)
print(person1["name"])
print(person1["age"])

# print(person1["hobbies"])#this will throw an error as hobbies is not available inside person1

print(person1.get("hobbies",["dancing","fishing"]))
person1["name"]="John"
person1["hobbies"]=["dancing","fishing"]
print(person1)


#remove elements from a dictionary

person1.pop("hobbies")
print(person1)

#key

for key in person1:
    print(key)
    print(person1[key])


#task

synonyms={"mountains":"peak","forest":"jungle"}
print("1.",synonyms["mountains"])
synonyms["terrain"]="land"
print("2.",synonyms)
synonyms.pop("forest")
print("3.",synonyms)

#Set

animals={"dog","cat","tiger","elephant","dog"}#even though animals has two dogs but in output we will see only one because set avoids duplicate
print(animals)

#add items to a set

animals.add("monkey")
print(animals)

animals={"dog","cat","elephant"}
wild_animals={"tiger","leopard","elephant"}
animals.update(wild_animals,{"dolphin"})
print(animals)

#remove item
animals.discard("dog")
animals.remove("cat")
print(animals)

animals.clear()
print(animals)

#set operation

domestic_animals={"dog","cat","elephant"}
wild_animal={"lion","tiger","elephant"}
animals_result=domestic_animals.union(wild_animal)
animals_result2=wild_animal.intersection(domestic_animals)
print(animals_result)
print(animals_result2)

#Range function

result=range(1,11)
print(list(result))

for value in range(1,6):
    print(value)

result1=list(range(1,11,3)) # here 3 defines how many numbers it will skip like o/p = 1,4,7,10
print(result1)

#can you create a list like this using the range function
#[3,6,9,12,15,18,21,24,27,30]

result2=list(range(3,31,3))
print(result2)

