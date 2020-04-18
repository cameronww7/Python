from __future__ import print_function

"""
 Prompt 35 While Loops 
"""

print("35 While Loops")

"""
while Loops
The while statement in Python is one of most general ways to 
perform iteration. A while statement will repeatedly execute 
a single statement or group of statements as long as the condition 
is true. The reason it is called a 'loop' is because the code 
statements are looped through over and over again until the 
condition is no longer met.

The general format of a while loop is:

while test:
    code statements
else:
    final code statements

Let’s look at a few simple while loops in action.
"""

# --------------------------------------------------
x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

# --------------------------------------------------

x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

else:
    print('All Done!')

# --------------------------------------------------
"""
break, continue, pass
We can use break, continue, and pass statements in our loops 
to add additional functionality for various cases. The three 
statements are defined by:

break: Breaks out of the current closest enclosing loop.

continue: Goes to the top of the closest enclosing loop.

pass: Does nothing at all.


Thinking about break and continue statements, the general 
format of the while loop looks like this:

while test: 
    code statement
    if test: 
        break
    if test: 
        continue 
else:

break and continue statements can appear anywhere inside the 
loop’s body, but we will usually put them further nested in 
conjunction with an if statement to perform an action based 
on some condition.

Let's go ahead and look at some examples!
"""

x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('x==3')
    else:
        print('continuing...')
        continue

# --------------------------------------------------

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

# --------------------------------------------------
