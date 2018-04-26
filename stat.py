#Christo Dragnev
#4/26/18
#stat.py

numbers = input('Type a list of numbers: ').split(' ')

for num in numbers:
    print(num)

print('Min: ',min(numbers))
print('Max: ',max(numbers))
print('Mean: ', sum(numbers)/len(numbers))
