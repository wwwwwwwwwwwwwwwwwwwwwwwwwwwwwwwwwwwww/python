data=['a','b','c',['abcd','efg']]
print(data[0])
print(data[-1])
print(data[-1][-1])
b=[1,2,3]
c=['Life','is','a','bitch']
f=b+c
print(f)
g=['a','b','c','d']
g[0]='f'
g[1]=['greenjoa','greenhate']
print(g)
g[1:2]=['greenjoa','greenhate']
print(g)
login=['naiveplanted','meme92','meme9206']
login.insert(1,'1234')
login.insert(3,'2345')
login.insert(5,'3456')
print(login)
info=['tom','hang','ks']
login.insert(2,info[0])
login.insert(5,info[1])
login.insert(8,info[2])
print(login)

for steps in range(9) :
    print(login[steps])



sc=[55,24,53,11,95,10,30,40]
sc.sort()
print(sc)
sc.reverse()
print(sc[0:5])
for steps in range(4):
    if isinstance(steps,list):
        for step in steps:
            print(steps)
    else:
        print(steps)

print(extend(list))