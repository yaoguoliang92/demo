#hex()  返回16进制
n1 = 255
print(str(hex(n1)))
print('-----')
def absDef(num):
	if not isinstance(num,(int,float)):
		raise TypeError('self write type Error')
	if num>0:
		return num
	else:
		return -num	

absDef('ateset')









