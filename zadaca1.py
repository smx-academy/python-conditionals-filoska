# Напишете програма која ќе прочита два броја од корисникот 
# и ќе го испечати збирот, разликата, производот и количникот на двата броја. 
# Споредете кој резултат е поголем, збирот или производот

broj1 = float(input('vnesete broj: '))
broj2 = float(input('vnesete broj: '))
zbir = broj1 + broj2 
razlika = broj1 - broj2
kolicnik = broj1 / broj2
proizvod = broj1 * broj2

print(f'Zbirot na {broj1} i {broj2} e {zbir}. \n Razlikata na {broj1} i {broj2} e {razlika}. \n Kolicnikot na {broj1} i {broj2} e {kolicnik}. \n Proizvodot na {broj1} i {broj2} e {proizvod}.')

if proizvod > zbir:
    print('Proizvodot e pogolem od zbirot.')
else:
    print('Zbirot e pogolem od proizvodot.')