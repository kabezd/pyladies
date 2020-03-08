# Tento program rozdává naivní rady do života.

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
bohata_retezec = input('Jsi bohatá? ')

if (stastna_retezec == 'ano' and bohata_retezec == 'ano'):
    print('Gratuluji!')
elif (stastna_retezec == 'ano' and bohata_retezec == 'ne'):
    print('Zkus míň utrácet.')
elif (stastna_retezec == 'ne' and bohata_retezec == 'ne'):
    print('Zkus se víc usmívat.')
else:
    print('Nerozumím!')