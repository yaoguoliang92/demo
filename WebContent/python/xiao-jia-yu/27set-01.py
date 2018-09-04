num={}
num2={1,2,3,4,5,6}
print(type(num2)) #class 'set'
#创建 1.直接用{}2.工厂函数set
set1 = set('abcde')
set2 = set([1,3,4,5,6])
print(set1)
print(set2)


#去重
num1=[1,2,3,1,1,1,1,0]
num1=list(set(num1))
print(num1)#注意 排序，set之后顺序打乱
print(1 in num1)

#add
#remove

set2 = (set(num1))
set2.add(123)
print(set2)

frozenset()
