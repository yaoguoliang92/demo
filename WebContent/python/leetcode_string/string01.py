# 反转字符串
class Solution:
	def reverseString(self, s):
		s = s[::-1]
		return s
		
	def reverseString2(self, s):
		lis=[]
		for i in range(len(s)):
			lis.append(s[len(s)-i-1])
		return "".join(lis)
	print(reverseString2(1,'abcdefg'))		
