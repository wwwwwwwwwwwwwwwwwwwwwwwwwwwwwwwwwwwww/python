class movie:
    count =0
    title ="암살       "
    director ="최동훈"
    def __init__(self,title,director):
        self.title = title
        self.director = director
        self.count+=1
        print(self.title+"생성자 호출")

    def __del__(self):
        print(self.title+"소멸자 호출")

    def showinfo(self):
        print(self.title+" "+self.director)

    @staticmethod
    def showCount():
        print(movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)


m1 = movie("암살","최동훈")
m2 = movie("베테랑","류승완")
#m3 = movie("사도","이준익")
#m4 = movie("인사이드 아웃","이택용")
#print(type(m4))
#m4=m3
#m4.showinfo()

print(m1.count)
print(m2.count)