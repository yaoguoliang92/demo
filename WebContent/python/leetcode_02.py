class Solution:
	def maxProfit(self, prices):
		i=0
		sum = 0
		count =0
		for x in range(1,len(prices)):
			#print(prices[x],':',prices[i])
			if prices[x]>prices[i]:
				sum=prices[x]-prices[i]
				count=sum+count
			i=i+1	
		print(count)	
		return count


	maxProfit(1,[7,6,4,3,1])
