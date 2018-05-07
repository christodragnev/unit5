#Christo Dragnev
#5/7/18
#quiz5.py

def penultimate(L1):
    print(L1[-2])
    
def plusEquals(a,b):
    new = []
    for item in a:
        new.append(item+b)
    print(new)
    
def smallest(L2):
    L2.sort()
    print(L2[0])
    
    
penultimate([3,4,5,6,7])
plusEquals([1,2,3,4],10)
smallest([1,2,3,4])
