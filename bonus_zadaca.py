# Да се напише програма која ќе прочита година од корисникот 
# и да одреди дали е годината престапна 
# (разгледајте и размислете како може да се креира вакво нешто)

godina = int(input('Vnesete godina: '))

if godina % 100 == 0:
    if godina % 400 == 0:
        print('Godinata e prestapna.')
    else:
        print('Godinata ne e prestapna.')
elif godina % 4 == 0:
    print('Godinata e prestapna.')
else:
    print('Godinata ne e prestapna.') 
