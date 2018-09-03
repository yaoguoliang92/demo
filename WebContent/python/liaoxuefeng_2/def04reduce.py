from functools import reduce
def fn(x,y):
	return x*10+y

def char2num(s):
	dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return dic[s]
	
print(reduce(fn,map(char2num,'2310')))	
