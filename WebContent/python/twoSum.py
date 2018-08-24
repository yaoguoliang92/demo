def twoSum(nums, target):
    dic={}
    for i,x in enumerate(nums):
        j=target-x
        if j in dic:
            return [dic[j],i]
        else:
            dic[x]=i
        print ('dic',dic)
print('-----------------------------');           
    

print(twoSum([55,3,2,7],9))    