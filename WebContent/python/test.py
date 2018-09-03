#li = [1,2,3,4,4,4]
#for f in range(1,len(li)):
#	print(f,':',li[f])
#str_x = 'abcde'
#str_x = str_x[:1]
#print(str_x)	


import collections
class Solution:
	def singleNumber(self, nums):
		dict = collections.Counter(nums)
		for i in range(len(nums)):
			if dict[nums[i]]==1:
				print(nums[i])
	singleNumber(1,[4,1,2,1,2])
