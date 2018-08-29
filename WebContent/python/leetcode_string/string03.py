# 字符串中的第一个唯一字符
import collections
class Solution:
	def firstUniqChar(self, s):
		dict=collections.Counter(s)
		for i in range(len(s)):
			if dict[s[i]]==1:
				return i
		return -1				


	print(firstUniqChar(1,'aaabbbc'))
