# x = 10
# print(type(x))
# x += 1 # x = x + 1
# print(x)
# x -= 1 # x = x - 1
# print(x)
# x /= 3 # x = x / 3
# print(x)
# x *= 5 # x = x * 5
# print(x)
# print(type(x))

# name = 'Roberto'
# age = 19
# print(len(name))
# print(name, 'is', age, 'years old.')
# print('{} is {} years old.'.format(name,age))
# print(f'{name} is {age} years old.')

# v = 5 < 3
# print(v)
# v = 3 > 1
# print(v)
# print(type(v))
# print(v)
# v = (not 5 < 10) or 3 > 5
# print(v)

# name = input('What\'s your name?\n')
# cadena = f'{name} 23456789'
# printf(cadena)
# age = int(input(f'Hi {name}, how old are you?\n'))

# if age < 0:
#     print('Error! An age cannot be negative')
# elif age < 18:
#     print('You shall not pass.')
# else:
#     print('You are allowed to pass.')


char = input('Type a letter: ').lower()
#{variable}.lower() ... minúscula
#{variable}.upper() ... mayúscula
if len(char) == 1:
    if char == 'a' or char == 'e' or char == 'i'\
        or char == 'o' or char == 'u':
        print('The letter you have typed is a vowel')
    else:
        print('The letter you have typed is consonant')
else:
    print('You must type a letter')        