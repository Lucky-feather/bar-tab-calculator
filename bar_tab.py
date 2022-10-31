#calc area of a cirlcle

##radius = input('enter radius')
#input is a string.  need int wrapped to convert string to number
#area = 3.142*int(radius)**2
#print('the area of your circle is', area)

#age = int(input('enter your age: '))

#if age < 10:
  # code block
 # print('you are too young for margaritas')

# age = 25
# num = 0

# while num < age:
#   if num % 2 == 0:
#     print(num)
#   if num == 5:
#     print(num,'golden riinggsss!')
#   num +=1

class Tab:

  menu = {
    "wine": 5,
    "beer": 3,
    "soda": 2,
    "chicken": 10,
    "beef": 15,
    "veggie": 12,
    "dessert":6
  }

def __init__(self):
  self.total = 0
  self.items = []

def add(self, item):
  self.items.append(item)
  self.total += self.menu(item)

def print_bill(self, tax, service):
  tax = (tax/100) * self.total
  service = (service/100) * self.total
  total = self.total + tax + service

for item in self.items:
  print(f'{item} ${self.menu[item]}')

print(f'{'Total'} ${total:.2f}')