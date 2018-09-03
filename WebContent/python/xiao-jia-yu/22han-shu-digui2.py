def factorial(n):
	if n==1:
		return 1
	else:
		return n * factorial(n-1)	
number = int(input("请输入"))
res = factorial(number)
print("%d 的阶乘是 %d" % (number,res))
