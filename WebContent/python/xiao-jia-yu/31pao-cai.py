#泡菜模块
#把所有对象转化为二进制流
#城市city字典大，用泡菜解决。程序变小
import pickle
my_list = [123,2.21,'sdffdd',['another list']]
pickle_file = open('my_list.pkl','wb')#新建文件  写bite
pickle.dump(my_list,pickle_file)#倒进去
pickle_file.close()
#结束->写成功


#开始读
pickle_file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)










