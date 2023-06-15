rios = {'nilo': 'Egito','negro': 'Brasil','amazonas': 'Barsil'}

for nome, pais in rios.items():
    if nome == 'nilo':
        print(f'O rio {nome} corre pelo {pais}')
    elif nome == 'negro':
        print(f'O rio {nome} corre pelo {pais}')
    elif nome == 'amazonas':
        print(f'O rio {nome} corre pelo {pais}')
print('#'*20)
for nome in rios.keys():
    print(f'O rio {nome.title()}')
print('#'*20)
for pais in rios.values():
    print(pais.upper())