cont = 0
soma =0
for i in range(1, 31):
    if i % 3 == 0:
        cont += 1
        soma = soma + i
print(f'soma dos valores {soma} total de chamadas {cont}', end=' ')
        