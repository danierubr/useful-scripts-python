# List comprehension:
# Using for 
temps1 = [221, 330, 458]
newtemps1 = [temp/10 for temp in temps1]
print(f' Temperatures 1: {newtemps1}')

# Using for + if
# The -999 means 'no value'
temps2 = [221, 330, -9999, 458]
newtemps2 = [temp/10 for temp in temps2 if temp != -9999]
print(f' Temperatures 2: {newtemps2}')

# Using for + if + else. The order changes
temps3 = [221, 330, -9999, 458]
newtemps3 = [temp/10 if temp != -9999 else 0 for temp in temps3]
print(f' Temperatures 3: {newtemps3}')

