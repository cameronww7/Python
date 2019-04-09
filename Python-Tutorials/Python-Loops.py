# 5. Python Loops
print("Python Loops")

num = 9

prime = True

print("For")
for test in range(2,10):
    if num % test == 0 and num != test:
        print(num,"equals",test,"*",num/test)
        prime = False
if prime:
    print(num,"Is a Prime Number")
else:
    print(num,"Is not a Prime")

numbers = range(5,50,10)

print(numbers)

for number in numbers:
    print(number)

print("While")
test = 2
num = 17
prime = True

while prime:
    if num % test == 0 and num != test:
        print(num, "equals", test, "*", num / test)
        prime = False
    else:
        test = test + 1
    if test == 10:
        break


if prime:
    print(num,"Is a Prime Number")
else:
    print(num,"Is not a Prime")