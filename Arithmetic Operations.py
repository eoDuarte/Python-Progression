#5 - Write a program that reads an integer and returns its successor and predecessor
n = int(input('Write a number to know your successor and predecessor: '))
print('The PREDECESSOR of {} is {} and its SUCCESSOR is {}'.format(n, (n-1), (n+1)))

#6 - Create a program with write a number and add its double and square root
nu = int(input('Hi! Write a number to know  its double and square root: '))
d = nu * 2
sr = nu ** (1/2)
print('The double of {} is {} and its square root is {:.0f}'.format(nu, d, sr))

'''7 - Student average'''

name = input('Nome: ')
n1 = float(input('Write the first note: '))
n2 = float(input('Write the second note: '))
print(f'The Student {name} has his first grade {n1} and second grade {n2} where your average is {(n1+n2)/2}')

m = float(input('Write a number in meters to find its multiples and submultiples: '))
print(f'The measure {m} in meters corresponds to: ')
print(f'{m / 1000} Km')
print(f'{m / 100} Hm')
print(f'{m / 10} Dam')
print(f'{m * 10}Dm')
print(f'{m * 100}Cm')
print(f'{m * 1000}')

n = int(input('Enter a number to find out your multiplication table: '))
print('-' * 12)
print(f'{n} x 1 = {n*1:>2}')
print(f'{n} x 2 = {n*2:>2}')
print(f'{n} x 3 = {n*3:>2}')
print(f'{n} x 4 = {n*4:>2}')
print(f'{n} x 5 = {n*5:>2}')
print(f'{n} x 6 = {n*6:>2}')
print(f'{n} x 7 = {n*7:>2}')
print(f'{n} x 8 = {n*8:>2}')
print(f'{n} x 9 = {n*9:>2}')
print(f'{n} x 10 = {n*10:>2}')
print('-' * 10)

reais = float(input('How many real you have in your wallet? R$: '))
print('You have R$:{:.2f} and can buyr US$:{:.2f}'.format(reais, reais/6))

print('Welcome to the wall paint calculator!')

print('='*35)
L = float(input('Write the Length of the WALL: '))
H = float(input('Write the Higth of the WALL'))
print('To painter your wall of {:.2f}m² you will need of {:.2f} liter of paint.'.format(L * H, (L * H) / 2))

value = float(input('Enter a value to receive the discount: '))
discount = value * .05
print('The value R${:.2f} with a discount of the 5% is R${:.2f}'.format(value, value - discount))

salary = float(input('Write the salary to receive the increase: '))
increase = salary * .15 + salary
print('Congratulations your salary from {:.2f} is now {:.2f}'.format(salary, increase))

print('Welcome to degrees converter!')
ce = int(input('How many degrees Celsius is it now?ºC '))
c = ce / 5
f = 32
c = c * 9
f = f + c
print('{}ºC are {}ºF'.format(ce, f))

print('Check the total car rental payment')
days = int(input('How many days was the car rented? '))
km = float(input('How many kilometers have you driven the car?'))
print('Used car for {} and {}km you total pay is R${}'.format(days, km, days * 60 + km * 0.15))
