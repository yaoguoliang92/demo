f = open("D:\\test.txt",'r')
#print(list(f))
#print(f.read(5))

f.seek(0,0)
print('***********')
#官方提供的
for x in f:
	print(x)


#f.write("hello")
f.close()
