from __future__ import print_function
import PythonFunctionSupport

# Python Functions
print("Python Functions")


x = 10
y = 20

z = x * y

print(z)

temp = 'Enter a multiple of ten:'

a = 20
#a = input(temp)

b = a / 10

print(a,'divided by ten is',b)

print( range(10,a) )


base = input('Please enter the base value: ')
exponent = input('Please enter the exponent value: ')

PythonFunctionSupport.exp(base,exponent)

PythonFunctionSupport.printFib(23)

fibSeries = PythonFunctionSupport.calcFib(23)

print(fibSeries)