#Christo Dragnev
#5/4/18
#warmup15.py function that takes a list of numbers as an argument and returns a new list with each number doubled


def double(L):
    new = []
    for item in L:
        new.append(item*2)
    return new
    
    
#testing
print(double([1,2,3,4,5]))
    

