from __future__ import print_function

"""
 Prompt 50-Nested-Statements-and-Scope
"""

print("50-Nested-Statements-and-Scope")

"""
Nested Statements and Scope
Now that we have gone over writing our own functions, it's important 
to understand how Python deals with the variable names you assign. 
When you create a variable name in Python the name is stored in a 
name-space. Variable names also have a scope, the scope determines 
the visibility of that variable name to other parts of your code.
"""


x = 25

def printer():
    x = 50
    return x

print(x)


print(printer())


"""

Interesting! But how does Python know which x you're referring to 
in your code? This is where the idea of scope comes in. Python has 
a set of rules it follows to decide what variables (such as x in 
this case) you are referencing in your code. Lets break down the rules:

This idea of scope in your code is very important to understand 
in order to properly assign and call variable names.

In simple terms, the idea of scope can be described by 3 general rules:

Name assignments will create or change local names by default.
Name references search (at most) four scopes, these are:
local
enclosing functions
global
built-in
Names declared in global and nonlocal statements map assigned 
names to enclosing module and function scopes.
The statement in #2 above can be defined by the LEGB rule.

LEGB Rule:

L: Local — Names assigned in any way within a function (def or 
lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any 
and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module 
file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names 
module : open, range, SyntaxError,...

"""


# x is local here:
num1 = lambda x:x**2

print(num1)

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()



"""
The global statement
If you want to assign a value to a name defined at the top level 
of the program (i.e. not inside any kind of scope such as functions 
or classes), then you have to tell Python that the name is not local, 
but it is global. We do this using the global statement. It is 
impossible to assign a value to a variable defined outside a 
function without the global statement.

You can use the values of such variables defined outside the 
function (assuming there is no variable with the same name within 
the function). However, this is not encouraged and should be avoided 
since it becomes unclear to the reader of the program as to where 
that variable’s definition is. Using the global statement makes it 
amply clear that the variable is defined in an outermost block.
"""

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
