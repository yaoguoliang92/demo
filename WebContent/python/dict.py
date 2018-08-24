def fan(num):
    for i,x in enumerate(num):
        print i,':',x,'----',num[x]
        
print fan({1:33,2:44,3:55})       