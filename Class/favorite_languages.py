from collections import OrderedDict

favorite_laguages = OrderedDict()
favorite_laguages['jen'] = 'python'
favorite_laguages['boyang'] = 'python'
favorite_laguages['lisa'] = 'C#'

for name, language in favorite_laguages.items():
    print(name.title() + "'s favorite language is : " + language.title() + "!")
from random import randint
x = randint(1, 6)
