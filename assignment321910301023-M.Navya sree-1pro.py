mystring = 'Hello, you need to print words which starts with s only in this sentense.'

for word in mystring.split():
    if word[0] == 's':
        print(word)
