import pizza
# import the entire function
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

# import sepcific functions
from pizza import make_pizza
make_pizza(20, 'tuna fish', 'mushrooms', 'potato', 'tomato')

# as the alias  
from pizza import make_pizza as mp
mp(25, 'tuna fish', 'potato', 'tomato')

# import all functions in the module 
from pizza import *
make_pizza(25, 'tuna fish', 'tomato', 'cheese')

# tips
# function names should be specified
# functions should contain annotations and document strings 
# all imports should be at the beginning
# ......