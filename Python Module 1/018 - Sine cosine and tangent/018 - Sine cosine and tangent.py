from math import sin, cos, tan, radians
angler = int(input(' Write a angle: º'))
angle = radians(angler)
sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)
print('The angle {} have {:.2f} with sine, {:.2f} with cosine and {:.2f} with tangent'. format(angler, sine, cosine, tangent))