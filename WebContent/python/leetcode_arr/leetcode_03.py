#旋转数组
#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution:
	def rotate(self, nums, k):
		nums_len = len(nums)
		nums[:] = nums[nums_len - k :] + nums[:nums_len - k]
		print(nums[:])
		
	rotate(1,[1,2,3,4,5,6,7],4)
