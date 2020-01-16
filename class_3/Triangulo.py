import math 
radio = float(input('Ingrese el radio del círculo: '))
if radio < 0:
    print('Dumbass! Radios cannot be negative')
else:    
    area = round(math.pi*radio**2, 2)
    print (f'El área del circulo es: {area}')