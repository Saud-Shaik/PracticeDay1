#Discount
fee=4535
discount_percent=10
discount_amount=(discount_percent/100)*fee
discounted_fee=fee-discount_amount
print("Fee after discount :",discounted_fee)

#Can you create a program to convert distance in kilometers to miles

distance_km=564.5
conversion_ratio=0.621371
distance_miles=distance_km*conversion_ratio
print(distance_miles)

#Passing Score
score=int(input("Enter your score :"))
if score >100 or score < 0:
 print("Invalid score")
elif score >=50:
 print("Congratulations")
 print("you have passed your exam")
else:
 print("Sorry!, you have failed your exam")

#Positive number or negative number
number=float(input("Enter a number :"))
if number > 0:
  print("Positive integer")
elif number < 0:
  print("Negative integer")
else:
  print("The number is 0")