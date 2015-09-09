dic1 ={}
dic2=dict()
dic={"name":"Pey",'phone':'01091929323','birth':"1118"}
a={1:'hi'}
b={'a':[1,2,3]}
print(dic['name'])

a={1:'a'}
a[2]='b'
a['name']='pey'
a[3]=[1,2,3]


c={"name":"Pey",'phone':'01042319323','birth':"0112"}
k=c.keys()
print(k)
k=list(c.keys())

c={"name":"Pey",'phone':'01042319323','birth':"0112"}
k=c.values()
print(k)

c={"name":"Pey",'phone':'01042319323','birth':"0112"}
k=c.items()
print(k)

movie={}
mov={"홍길동":{'베테랑':'4.0','암살':'2.0'},'고길동':{'베테랑':'2.0','암살':'2.0'}}
name=mov.keys()
print(name)
star=mov.values()
print(star)


print(mov['홍길동']) #홍길동이 별점준 영화목록
print(mov['홍길동']['암살']) #홍길동이 암살에 매긴 별점


#answer = input("would you like express shipping?")
#if answer.lower() == "yes" :
#    print("That will be an extra $10")
    

for steps in range(9):
    print(steps+1,'단')
    for steps2 in range(9):
        print('%d x %d = %d'%(steps+1,steps2+1,(steps+1)*(steps2+1)))
    
import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)

import turtle
nSides=5
for steps in range(nSides):
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides):
        turtle.forward(50)
        turtle.right(360/nSides)
