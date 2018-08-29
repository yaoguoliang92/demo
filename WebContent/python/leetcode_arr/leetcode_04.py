#  存在重复
#给定一个整数数组，判断是否存在重复元素。

#如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
#
class Solution:
	def containsDuplicate(self, nums):
		s = set(nums)
		nums_len = len(nums)
		s_len = len(s)
		if nums_len==s_len:
			return False
		else:
			return True	



	print(containsDuplicate(1,[1,2,3,4]))        