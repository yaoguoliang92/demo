#加一
#给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
class Solution:
	def plusOne(self, digits):
	#数组转换成数字
		intNum=0
		for i in range(len(digits)):
			intNum=intNum*10+digits[i]
			print(intNum)	
		intNum+=1
		#数字转换成字符
		strNum=str(intNum)
		#字符转换成数组
		res=[]
		for i in range(len(strNum)):
			res.append(int(strNum[i]))
		return res

	print(plusOne(1,[3,3,1]))
