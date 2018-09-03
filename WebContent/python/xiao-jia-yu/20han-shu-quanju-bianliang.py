def func():
	global count		#变为全局
	count =10
	print(10)


def fun1():
	print('func1')
	def fun2():
		print('func2')
	fun2()
fun1()	

#fun2访问不到
#----------------
#闭包
def FunX(x):
	def FunY(y):
		return x*y
	return FunY 
	
print(FunX(8)(5))	


def func1():
	x=5
	def func2():
		nonlocal x    #用list[]也可以
		x*=x
		return x
	return func2()
func1()		
print(x)
