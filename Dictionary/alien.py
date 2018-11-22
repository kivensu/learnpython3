'''
alien_01 = {'color': 'green', 'points': 5}
alien_02 = {'color': 'red', 'points': 10}
alien_03 = {'color': 'blue', 'points': 15}
aliens = [alien_01, alien_02, alien_03]
for alien in aliens:
    print(alien)
'''
aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print ("....")