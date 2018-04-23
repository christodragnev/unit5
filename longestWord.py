#Christo Dragnev
#4/23/18
#longestWord.py

words = input('Enter a list of words: ').split(' ')

for item in words:
    long = len(item)
    print('The longest word is ',max(long))
