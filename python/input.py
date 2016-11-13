# name = raw_input ('What is your name? ')
# print('Hi ' + name)

# name = raw_input('What is your name?')
cost = raw_input('How much was your meal?')
tip = float(cost) * .2
total_cost = float(cost) + float(tip)
print('You should tip $' + str(tip) + '.')
print('Your total cost would be $' + str(total_cost) + '.')