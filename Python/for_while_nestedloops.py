# while loop in python
count = 0
while (count < 3 ): # condition -> statment -> else
    count += 1
    print("count" , count)
else:
    print("Pankaj Singh Rawat")

# for loop in python
n = 4
for i in range(0,n):
    print("number:",i)

print("list iteration")
l = ["Pankaj" , "Singh" , "Rawat"]
for i in l:
    print(i)

# iteration using index 
for i in range(len(l)):
    print(l[i])
else:
    print("Why else WHYYYY")

# Nested Loops
for i in range (1, 5):
    for j in range (i):
        print("*" , end=" ")
    print()