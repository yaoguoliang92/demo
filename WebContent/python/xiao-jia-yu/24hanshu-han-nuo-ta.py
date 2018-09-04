def hanoi(n,x,y,z):#n:盘子数量,xyz三根针
	if n==1:
		print(x,'--->',z)
	else:
		hanoi(n-1,x,z,y)##将前n-1个盘子从x移动到y上
		print(x,'--->',z)#将最地下最后一个盘子从x移动到z上
		hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
n=int(input('input:'))
hanoi(n,'x','y','z')
