unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    corrent_user = unconfirmed_users.pop()
    print(f'Verificando usúario : {corrent_user}')
    confirmed_users.append(corrent_user)
print('\nUSUÁRIOS VERIFICADOS\n')
for user in confirmed_users:
    print(f'Usúarios verificados: {user.title()}')