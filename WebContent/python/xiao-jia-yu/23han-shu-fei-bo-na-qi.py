def func(n):
	n1=1
	n2=1
	n3=1
	if n<1:
		print('error')
		return -1
	while(n-2)>0:
		n3=n1+n2
		n1=n2
		n2=n3
		n=n-1
	return n3
	
result = func(20)
if result!=-1:
	print('总生了%d个兔子'%result)	
			


def func_digui(n):
	if n<1:
		print('error')
		return -1
	if n==1 or n==2:
		return 1
	else:
		return func_digui(n-1)+func_digui(n-2)
result2 = func_digui(35)
if result2 != -1:
	print("digui:%d" % result2)
			
	
