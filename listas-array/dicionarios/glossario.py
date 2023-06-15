glossario = {
    'python': 'Melhor linguagem do mundo',
    'django': 'O melhor framework web',
    'javascript': 'Linguagem de programação',
    'html': 'Linguagem de marcação',
    'css': 'Linguagem de estilização',          
              }
glossario['java'] ='liguagem de programação'
glossario['c++'] ='liguagem de programação da microsoft'
glossario['c'] ='liguagem de programação muito dificil'
    
           


for key, values in glossario.items():
    print(f'{key.title()}: {values}')