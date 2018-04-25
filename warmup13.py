#Christo Dragnev
#4/25/18
#warmup13.py - making a list of 20 random numbers between 1 and 100

from random import randint

myList = []

i=0
while i<=20:
    myList.append(randint(1,100))
    i+=1
print(myList)

print(sum(myList))
print(max(myList))
print(min(myList))
    