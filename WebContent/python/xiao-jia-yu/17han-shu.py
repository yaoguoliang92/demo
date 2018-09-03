def func(name='xiaoming'):
	return name
print(func())
print('-------------')
def test(x,y,*params):
	print('first:',params[0])
	print('length:',len(params))
	
test(1,2,3,'xiaoming')	