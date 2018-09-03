#import sys
#sys.setrecursionlimit(10000) #设置层


def recursion(n):
	result=n
	for i in range(1,n):
		result*=i
	return result
number = int(input("请输入："))
result=recursion(number)	
print("%d 的阶乘是 %d" % (number,result))		
	 
