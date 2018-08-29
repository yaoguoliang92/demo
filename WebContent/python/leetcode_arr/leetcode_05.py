 #只出现一次的数字
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

class Solution:
	def singleNumber(self, nums):
		s=set([])
		for x in nums:
			if x in s:
				s.remove(x)
			else:
				s.add(x)	
			
		return list(s)[0]
	
	def singleNumber2(self, nums):
		s={}
		for x in nums:
			if x in s.keys():
				s.pop(x)
			else:
				s[x]=1	
			
		return list(s.keys())[0]	
	
	#最牛
	#异或：两者相等为0,不等为1.
	def singleNumber3(self, nums):
		res=0
		for x in nums:
			print(res,':',x)
			res=res^x
		return res
	
	print(singleNumber3(1,[5,2,3,4,2,3,4]))
