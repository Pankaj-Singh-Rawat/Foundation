# using if else in python

a = 35 
b = 40 
if( a > b):
    print(a)
else:
    print(b)

# using elif in python 

c = 333

if (a > b):
    print(a)
elif (b>c):
    print(b)
elif(c>a):
    print(c)


# short hand if
if (b>a) : print("a is smaller")
print(a) if a > b else print("b is greater than a")

# using and

if c > b and c > a:
    print(c)

# using or

if a > b or c > b :
    print("one of them is greater than b")

# using not 

if not a > b:
    print("b is greater")


# pass statement

if a > b:
    pass