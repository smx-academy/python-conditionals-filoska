# Напишете програма која ќе прочита број од корисникот 
# и ќе го провери дали тој е деллив со 3, 5, 3 и 5, 
# а потоа ќе испечати соодветната порака.

broj = int(input('Vnesete broj: '))

if broj % 3 == 0:
    print(f'Brojot {broj} e deliv samo so 3.')
elif broj % 5 == 0:
    print(f'Brojot {broj} e deliv samo so 5.')
elif broj % 3 == 0 and broj % 5 == 0:
    print(f'Brojot {broj} e deliv i so 3 i so 5.')
else:
    print(f'Brojot {broj} ne e deliv niti so 3 niti so 5.')