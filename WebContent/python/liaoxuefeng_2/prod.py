#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：

#coding: utf-8
from functools import reduce
def prod(L):
	def _product(x,y):
		return x*y
	return reduce(_product,L)	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('success!')
else:
    print('fail!') 