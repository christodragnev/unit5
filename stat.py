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

L.count(item)
print('Median:',
