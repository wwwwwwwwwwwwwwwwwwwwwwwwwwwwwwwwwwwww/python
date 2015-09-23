##coding:cp949
#from abc import abcmeta, abstractmethod
#class terran(metaclass=abcmeta):
#    def __init__(self , name):
#        self.name = name
#    @abstractmethod
#    def attack(self):
#        pass
#   
#class tank(terran):
#    def __init__(self , name , damage):
#        super().__init__(self , name)
#        self.damage = damage
#    def attack(self):
#        print("탱크를 쏩니다.")
#class marine(terran):
#    def __init__(self , name , hp):
#        super().__init__(self , name)
#        self.hp = hp
#    def attack(self):
#        print("총을 쏩니다.")
#def attack(terran):
#    terran.attack()
#t1 = tank("tank",500)
#t2 = marine("marine" , 100)
#tlist = [tank("tank1",500), tank("tank2",500),marine("marine1",100)]
#for item in tlist:
#    attack(item)
# 
#
#attack(t1)
#attack(t2) 
#
class MyList(list):
    name = ""
    def __init__(self,name):
        super().__init__([])
        self.name = name 
    def __str__(self):
        return self.name+";"+super().__str__()

list1 = MyList("greenjoa")
list1.append(10)
list1.append(40)
list1.append(30)
list1.append(20)
list1.append(60)

print(list1)