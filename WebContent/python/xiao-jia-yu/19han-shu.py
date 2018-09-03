#变量作用域
def func(num1):
	num2=30		#python会在局部中复制全局变量，自动创建内部用
	print(num1)
	print(num2)
	
num2=20
func(10)
print(num2);	 
