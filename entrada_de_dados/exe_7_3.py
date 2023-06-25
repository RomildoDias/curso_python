number = input('Digite um número: ')
number = int(number)

if number % 10 == 0:
    print(f'O número {number} é multiplo de 10')
else:
    print(f'O número {number} não é multiplo de 10')