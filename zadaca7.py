# Напишете програма која ќе прочита големина на агли во триаголник, 
# да се провери дали може да се формира триаголник со тие агли(збирот мора да биде 180) 
# и ако може да се формира триаголник да се провери каков триаголник може да се формира

agol1 = int(input('Vnesete agol vo triagolnik: '))
agol2 = int(input('Vnesete agol vo triagolnik: '))
agol3 = int(input('Vnesete agol vo triagolnik: '))

if agol1 + agol2 + agol3 == 180:
    if agol1 == 60 and agol2 == 60 and agol3 == 60:
        print('Moze da se formira ramnostran triagolnik.')
    elif agol1 == agol2 or agol1 == agol3 or agol2 == agol3:
        print('Moze da se formira ramnokrak triagolnik.')
    elif agol1 != agol2 and agol1 != agol3 and agol2 != agol3:
        print('Moze da se formira raznostran triagolnik.')
else:
    print('Ne moze da se formira triagolnik.')
