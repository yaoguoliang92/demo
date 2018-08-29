class Solution:
	def intersect(self, nums1, nums2):
		ls=[]
		for x in nums1:
			if x in nums2:
				ls.append(x)
				nums2.remove(x)

		return ls        