favorite_lenguages = {'jen':'python','sarah':'cs','edward':'ruby','phil':'python',}
friends =['Romildo', 'jen', 'sarah', 'phil', ]

for name in favorite_lenguages.keys():
    if name in friends:
        print(name,' obrigado por respoder a enquente.')
    else:
        print(name,' Por favor responda nossa enquete.')
