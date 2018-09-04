dict1={}
dict1.fromkeys((1,2,3))
print(dict1)
dict1=dict1.fromkeys((1,2,3),'haha')
print(dict1)
#fromkeys()

#items
dict3={'A':65,'B':66}
for x in dict3.items():
	print(x)
print('---------')
for k,v in dict3.items():
	print(k,':',v)

print(dict3.popitem())#随机
#keys()
#values()
#update()

dict5={'C':67}
dict3.update(dict5)
print(dict3)
