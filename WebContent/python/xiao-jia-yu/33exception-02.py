try:
	f = open('1.txt')
	#print(f.read())
	f.write("hello")
#except OSError as reason:
#	print('file error:::',str(reason))
#except TypeError as reason:
#	print(str(reason))	
except (OSError,TypeError) as reason:
	print('error:',reason)	
finally:
	f.close()
	

raise RuntimeError('自定义解释这个异常')
