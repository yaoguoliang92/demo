# 颠倒整数
class Solution:
	def reverse(self, x):
		reverse_num = int(str(abs(x))[::-1])
		if reverse_num.bit_length()>31:
			return 0
		else:
			return reverse_num if x>0 else -reverse_num
	    	
	    	
	print(reverse(1,15342469))    