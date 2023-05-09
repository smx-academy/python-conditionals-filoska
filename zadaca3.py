# Напишете програма која ќе прочита број од корисникот 
# и ќе го провери дали тој е парен, 
# и потоа ќе испечати соодветната порака.

broj = int(input('Vnesete broj: '))

if broj % 2 == 0:
    print(f'Brojot {broj} e paren.')
else:
    print(f'Brojot {broj} e neparen.')