import math
def quadratic(a, b, c):
	aa = math.sqrt(b*b-4*a*c)
	return (-b+aa)/4*a*c,(b+aa)/4*a*c
	
print(quadratic(2, 3, 1))	
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))








