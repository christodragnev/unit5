#Christo Dragnev
#5/7/18
#quiz5.py

def penultimate(L1):
    return L1[-2]
    
def plusEquals(a,b):
    new = []
    for item in a:
        new.append(item+b)
    return new
    
def smallest(L2):
    L2.sort()
    return L2[0]
    
    
print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
