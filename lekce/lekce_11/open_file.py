# file_ = open("poem.txt", encoding='utf-8')
# content = file_.read()
# file_.close()

# print(content)

## bezpecnejsi moznost, ktera automaticky zavre subor po provedeni kodu
# je to pomoci "context manager" package/tridy
with open('poem.txt', encoding='utf-8') as file_:
    content = file_.read()

print(content)


print('I heard this poem:')
print()

with open('poem.txt', encoding='utf-8') as file_:
    for line in file_:
        print('    ' + line)

print()
print('Do you like it?')

#### lepsi nejprve strip bilych znaku radku a teprve pak vypsat
print('I heard this poem:')
print()

with open('poem.txt', encoding='utf-8') as file_:
    for line in file_:
        line = line.rstrip()
        print('    ' + line)

print()
print('Do you like it?')


with open('second-poem.txt', mode='w', encoding='utf-8') as file_:
    print('Naše staré hodiny', file=file_)
    print('Bijí', 2+2, 'hodiny', file=file_)


## mozna lepsi zpusob zapisovani:
with open('second-poem.txt', mode='w', encoding='utf-8') as file_:
    file_.write("test textu")