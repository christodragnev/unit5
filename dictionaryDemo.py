#Christo Dragnev
#4/25/18
#dictionaryDemo.py - more list practice

words = ['computer','mortifying','dog','firetruck','yes','python','cat']

words.sort()

num = int(input('What numberword do you want? '))

if num<=0 or num>=len(words)+1:
    print('Invalid number')
else:
    print(words[num-1])
