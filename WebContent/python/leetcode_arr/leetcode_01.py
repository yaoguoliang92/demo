class Solution:
    def removeDuplicates(self,nums):
        s=set([])
        for x in range(len(nums)):
            #print(nums[x])
            s.add(nums[x])
        #print('------------')
        #print(s)
        nums=list(s)
        print(nums)
        return len(nums)

    removeDuplicates(1,[1,1,2])	
    
    
"""    class Solution:
    def removeDuplicates(self, nums):

     
        if len(nums) <= 1:
            return len(nums)
        s = 0
        for f in range(1, len(nums)):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
        return s + 1
           """