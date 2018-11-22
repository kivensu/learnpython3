alien_01 = {'color': 'green', 'points': 5}
# print (alien_01['color'])
# print (alien_01['points'])
# new_points = alien_01['points']
# print ("Your just earned " + str(new_points) + " points!")
# print(alien_01)
alien_01['x_position'] = 0
alien_01['y_position'] = 25
alien_01['speed'] = 'medium'
# print("The alien_01 color is " + alien_01['color'] + "!")
# alien_01['color'] = 'yellow'
# print("The alien_01 new color is " + alien_01['color'] + "!")
# print(alien_01)
if alien_01['speed'] == 'slow':
    x_increment = 1
elif alien_01['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_01['x_position'] = alien_01['x_position'] + x_increment
print("The alien_01 new x_position is: " + str(alien_01['x_position']))
print(alien_01)
del alien_01['points']
print(alien_01)
