convidados = ['Fernanda', 'Nayra', 'Jasmyn']
lista ='' 
print(convidados[2] + ' convido você para jantar um a noite')
print(convidados[0] + ' convido você para jantar um a noite')
print(convidados[1] + ' convido você para jantar um a noite')
convidados[1] = 'Matheus'
print(convidados)
print('=' * 10 +' Desmarcou '+ '='*10)
print('Encontrei uma mesa maior então convidarei mais algumas pessoas')

convidados.insert(0, 'Matheus')
convidados.insert(1, 'Romildo')
convidados.insert(2, 'Hadassa')

print(convidados)

print('Pessaol sinto informar mais a mesa não chegara a tempo e so vou poder convidar duas pessoas')

matheus=convidados.pop(0)
print('=-='*30)
print(f'Desculpa mais não será possivel você conparecer ao jantar {matheus}.')
romildo=convidados.pop(1)
print(f'Desculpa mais não será possivel você conparecer ao jantar {romildo}.')
hadassa=convidados.pop(2)
print(f'Desculpa mais não será possivel você conparecer ao jantar {hadassa}.')

print('=-='*10 + 'CONVIDADOS' + '=-='*10)
print(convidados)

print('=-='*30)
print(f'Conto com sua presença no jantar {convidados[0]}')
print(f'Conto com sua presença no jantar {convidados[1]}')
print(' ')



