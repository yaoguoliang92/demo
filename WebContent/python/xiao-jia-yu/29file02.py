def redfile(filedir):
	file = open(filedir)
	for x in file:
		print(x[:3])
		print(x[3:])
		if x[:3]=='客服：':
			savefile('kf',x[3:])
		elif x[:3]=='甲鱼：':
			savefile('jy',x[3:])	
	file.close()
def savefile(str,line):
	boy_file=open('D:/jy.txt','a')
	girl_file=open('D:/kf.txt','a')
	if str=='kf':
		boy_file.writelines(line)
	else:
		girl_file.writelines(line)
	boy_file.close()
	girl_file.close()
redfile('D:/test.txt')	
