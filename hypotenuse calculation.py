from math import sqrt, hypot
ca = int(input('Who is the adjacent leg? '))
co = int(input('Who is opposite side?'))
h = hypot(ca, co)
print('With adjacent leg {} and opposite side {} the hypotenuse is {}'.format(ca, co, h))
