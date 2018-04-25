words = input('Enter a list of words: ').split(' ')

good = ''
for item in words:
    if len(item)>len(good):
        good = item
print(good)