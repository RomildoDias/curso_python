#alien_0 = {'color': 'green','poits': 5}
#alien_1 = {'color':'yellow','poits': 10}
#alien_2 = {'color':'red','poits':'15'}

#aliens = [alien_0,alien_1,alien_2]
#for alien in aliens:
    #print(alien)

aliens = []
for alien in range(30):
    new_alien = {'color':'green','poits':'5','speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['poits'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['poits'] ='15'
for alien in  aliens[:5]:
    print(alien)
print(f'Total de aliens criado foi {len(aliens)}.')

 