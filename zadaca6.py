# Напишете програма која ќе прочита страни на правоаголник и квадрат, 
# да се пресмета плоштината 
# и да се провери дали збирот на плоштините е деллив со 2,3 или 5

a = int(input('Vnesete strana na kvadrat: '))
b = int(input('Vnesete dolzina na pravoagolnik: '))
c = int(input('Vnesete sirina na pravoagolnik: '))
Pk = 2*a
Pp = b*c
zbir = Pk + Pp
 
if zbir % 2 == 0:
    if zbir % 3 == 0:
        if zbir % 5 == 0:
            print('Zbirot na plostinite e deliv so 2, 3 i 5.')
        else:
            print('Zbirot na plostinite e deliv so 2 i 3.')
    else:
        print('Zbirot na plostinite e deliv samo so 2.')
elif zbir % 3 == 0:
    if zbir % 5 == 0:
        print('Zbirot na plostinite e deliv so 3 i 5.')
    else:
        print('Zbirot na plostinite e deliv samo so 3.')
elif zbir % 5 == 0:
    print('Zbirot na plostinite e deliv samo so 5.')
else:
    print('Zbirot na plostinite ne e deliv niti so 2, niti so 3, niti so 5.')
