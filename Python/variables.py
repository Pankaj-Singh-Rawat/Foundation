# variables : those who store data types are called variables

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.


# Basic assignment of variables 
x = 5 
y = 3.14 
z = "Pankaj"

# Dynamic typing : using same variable and overwriting it's data type
x = 5 
x = "x is now a string , haha"

# assigning the same value
a = b = c = 100
print(a,b,c)

# type casting : converts value of one data type to another ( for eg: int -> float )
s = "10" #string type 
n = int(s) #changing from string to integer data type
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

print(n)  
print(cnt)  
print(s2)

#scope of a variable ( local and global )

def f():
    a = "I'm local"
    print(a) # a : is a locl variable cause it's is working only inside the function defined so it is only available locally to the function

a = 12 # this is a global varalble and can be used anywhere in the code block


#swapping two variables
a , b = 5 , 10 
print(a , b)
b , a = 5 , 10 
print(a , b)

# counting characters in a string

word = "Python"
length = len(word)
print(length)

# deleting a variable
del(word)
