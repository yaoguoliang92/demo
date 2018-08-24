def fan(num):
    for i,x in enumerate(num):
        print i,':',x,'----',num[x]
        
print fan({1:33,2:44,3:55})       


d = {
    95:'Adam',
    85:'Lisa',
    59:'Bart'
}

print d.get(95)

for key in d:
    print key,':',d[key]