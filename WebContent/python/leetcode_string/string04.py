#  有效的字母异位词
#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

#示例 1:

#输入: s = "anagram", t = "nagaram"
#输出: true
#示例 2:

#输入: s = "rat", t = "car"
#输出: false
#说明:
#你可以假设字符串只包含小写字母。

#进阶:
#如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
import collections
class Solution:
	def isAnagram(self, s, t):
		if len(s) == len(t):
			dict = collections.Counter(s)
			dict2 = collections.Counter(t)
			num=0
			for k,v in dict.items():
				print(k,v)
				if k in dict2 and v == dict2[k]:
					num+=1
			#if num==len(dict):
			#	return True
			#else
			#	return False
			return True if num==len(dict) else False 	
		else:
			return False			
	print(isAnagram(1,'abc','acb'))	