import random

# fibonnaci sequence

def fibonacci(n):
    if n <= 0 :
        return 0 
    
    list = []
    a , b = 0 , 1

    for i in range(n):
        list.append(a)
        a , b = b , a+b

    print(list)

fibonacci(5)


# random number guessing game 

random = random.randint(0,100)
guess = 0
while guess != random:
    guess = int(input("Guess the random number: "))

    if (guess < random):
        print("too low")
    
    elif (guess > random):
        print("too high")
    
    else:
        print("Correct guess! : " , guess , "is the correct random number")
        break
    
# leap year checker

leap_year = int(input("Enter a year : "))

if leap_year % 4 == 0 or leap_year % 100 == 0 and leap_year % 400 != 0 :
    print(leap_year , "is a leap year")
else :
    print(leap_year, "is not a leap year")

# prime number checker

num = 13

if num == 1:
    print("not a prime number")
else : 
    for i in range(2 , num):
        if num % i == 0:
            print("not prime number")
            break
        else :
            print("prime number") 
            break

# sum of digits 

num = 123 
ans = 0
for i in range(num):
    store = num % 10 
    ans += store 
    num = num // 10
print(ans)

# reverse a number

num = 12345
ans = 0 

while num > 0 :
    store = num % 10 
    num = num // 10 
    ans = (ans * 10) + store
print(ans)