#Christo Dragnev
#4/26/18
#vowelWords.py - how to treat strings as lists

words = input('Enter some words: ').split(' ')

for item in words:
    if item[0] in 'aeiouAEIOU': #starts with vowel
        print(item)

