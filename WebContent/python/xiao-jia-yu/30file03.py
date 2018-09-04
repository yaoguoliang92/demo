#模块
#import random
#num=random.randint(0,9)#
#print(num)


import os
print('path:',str(os.getcwd()))#当前目录
print('sep:',str(os.sep()))
#print(os.curdir())    #.	
#print(os.pardir())		#..

os.chdir('E:\\')	#cd 
os.listdir("E:\\")		#列举
os.mkdir('E:\\a\\')
os.remove(path)	#删除文件
os.rmdir(path)  #删除目录
os.removedirs(path) #递归删除
os.system('cmd')	#执行
os.curdir	#当前目录
os.pardir	#父级目录
os.listdir(os.curdir)#显示当前文件夹
os.set		#路径分隔符
os.path.basename(path)	#返回文件名去除路径
os.path.dirname(path)	#返回路径

