#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#输入: [0,1,0,3,12]
#输出: [1,3,12,0,0]

#必须在原数组上操作，不能拷贝额外的数组。
#尽量减少操作次数。
class Solution:
	def moveZeroes(self, nums):
		for i in range(len(nums)):
			if nums[i]==0:
				nums.remove(nums[i])
				nums.append(0)
		return nums

	def moveZeroes2(self, nums):
		j=0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[j],nums[i]=nums[i],nums[j]
				j+=1
			print(nums,'----',i)	
		return nums

	print(moveZeroes2(1,[0,1,0,3,12]))
