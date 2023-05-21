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
convidados.insert(3, 'Hadassa')

print(convidados)

