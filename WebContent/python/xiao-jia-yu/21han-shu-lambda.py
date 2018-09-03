def ds(x):
	return 2*x+1
lambda x:2*x+1

g=lambda x,y:x+y
print(g(3,4))

#内置函数filter过滤器，去掉非True的
print('=================')
def odd(x):
	return x%2
temp = range(10)
show = filter(odd,temp)
print(list(show))


print(list(filter(lambda x : x%2,range(10))))
print(list(range(10)))
print('=================')
#内置函数map
print(list(map(lambda x:x*2,range(10))))

