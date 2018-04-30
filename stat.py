#Christo Dragnev
#4/26/18
#stat.py

L = []
while True:
    number = input('Type a list of numbers: ')
    if number!='q':
        L.append(float(number))
    else:
        break
   

for num in L:
    print(num)

print('Min: ',min(L))
print('Max: ',max(L))
print('Mean: ', sum(L)/(len(L)))

good = ''
for item in L:
    if L.count(item)>L.count(good):
        good = item
        print('Mode: ',good)
        
L.sort()
if len(L)%2==0:
    print('Median: ',L[len(L)/2-1],L[len(L)/2])
else:
    print('Median: ',L[len(L)/2])