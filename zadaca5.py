# Напишете програма која ќе прочита два броја од корисникот 
# и ќе го испечати производот на броевите, 
# да се провери дали резултатот е парен или не парен.

broj1 = int(input('Vnesete broj: '))
broj2 = int(input('Vnesete broj:'))
proizvod = broj1 * broj2

print(f'Proizvodot na broevite {broj1} i {broj2} e {proizvod}.')

if proizvod % 2 == 0:
    print('Prozivodot e paren.')
else:
    print('proizvodot e neparen.')