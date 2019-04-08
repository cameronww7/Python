# 4. Python Input and Output
from __future__ import print_function

print("Python IO")

#end='' removes new line
print("test cats",end='')

# sep removed the spaces
print('test', '!!!!!',"----", sep='')


print("names")


#userName = input("Please Enter your Name: ")

#print('Sup', userName + "!")

userName = input("Please Enter your Name: ")
age = input("Please Enter your Age: ")


factor = 2
finalage = int(age) + factor
multAge = int(age) * factor
divAge = int(age) / factor

print("in", factor, "years you will be", finalage, "years old", userName)
print("Your age multipled by", factor, "is", multAge)
print("your age divided by", factor, "is", divAge)