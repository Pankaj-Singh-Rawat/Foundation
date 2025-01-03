#data types in python


#1. Numeric data type

a = 5   #integer
print(type(a)) # prints data type of a

b = 5.4 #float
print(type(b)) # prints data type of b

c = 2 + 4j #complex
print(type(c)) # prints data type of c


#2. Sequence data types in python

s = "Hey Pankaj" # string 
print(s)
print(s[5]) #accessing character of string at 5th index
print(s[-1]) #accessing string from backward direction via index


e = [] #Empty list 
l = [1,2,3] #list with values
print(l)
m = ["hey" , 5 , "string" , 6] #list with different data types
print(m)

# accessing list items 
print(m[0])
print(m[3])
print(m[-3])
print(m[-2])


# 3. Tuple data type

t0 = tuple() #empty tuple
t1 = tuple((1,2,3,4,5))
t2 = tuple(("string" , "is" , "here"))
print(t0)
print("tuple with the use of integers: " , t1)
print("tuple with the use of string: " , t2)


# 4. Boolean data type 

print(type(True))
print(type(False))

# 5. SET data type

s0 = set() # empty set
s1 = set("PankajSinghRawat")
print("Set with string type :" , s1)
s2 = set([1,2,3,4])
print("Set with integer type :" , s2)
s3 = set(["hey" , "how" , "are" , "you"])
print("here's how to print full strings: ", s3)

# accessing set items
set1 = set(["hey" , "how" , "are" , "you"])
for i in set1:
    print(i , end=" ")

print("\n")

#checking if something exists in set 

print("how" in set1)

# 6. Dictionary data type 

d = {} # empty dictionary
d1 = {1: 'Pankaj' , 2: "Singh" , 3: 'Rawat'}
print(d1)

# creating dictionary using dict() constructor
d2 = dict({'name': 'Pankaj' , 2: "Singh" , 3: 'Rawat'})
print(d2)

# accessing key value in dictonary

print(d2['name']) # using key
print(d1.get(3)) # using get