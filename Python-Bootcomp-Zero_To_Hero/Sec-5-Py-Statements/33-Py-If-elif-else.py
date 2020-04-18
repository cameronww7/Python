from __future__ import print_function

"""
 Prompt 33 if, elif, else Statements :
"""

print("33 if, elif, else Statements")

"""
if, elif, else Statements

if Statements in Python allows us to tell the computer to 
perform alternative actions based on a certain set of results.

Verbally, we can imagine we are telling the computer:

"Hey if this case happens, perform some action"

We can then expand the idea further with elif and else statements, 
which allow us to tell the computer:

"Hey if this case happens, perform some action. Else, if another 
case happens, perform some other action. Else, if none of the 
above cases happened, perform this action."

Let's go ahead and look at the syntax format for if statements to 
get a better idea of this:

if case1:
    perform action1
elif case2:
    perform action2
else: 
    perform action3
"""
# --------------------------------------------------
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')

# --------------------------------------------------
person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")

# --------------------------------------------------
person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person == 'George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")
