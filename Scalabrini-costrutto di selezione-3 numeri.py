V1 = int(input('inserisci un numero '))
V2 = int(input('inserisci un numero '))
V3 = int(input('inserisci un numero '))

if((V1 > V2) and (V1 > V3)):
    print('il maggiore dei numeri inseriti è ', V1)
elif((V2 > V1) and (V2 > V3)):
    print('il maggiore dei numeri inseriti è ', V2)
else:
    print('il maggiore dei numeri inseriti è ', V3)
    
