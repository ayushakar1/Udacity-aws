from shirt import Shirt

#entries

shirt_one = Shirt('red','M','long_sleeved',45)
shirt_two = Shirt('green','S','short_sleeved',30)

print(shirt_one.price)
print(shirt_one.color)

shirt_two.change_price(45)
print(shirt_two.price)

shirt_one.color = 'yellow'
shirt_one.size = 'L'

print(shirt_one)       #prints location of data in memory
print(shirt_one.size)