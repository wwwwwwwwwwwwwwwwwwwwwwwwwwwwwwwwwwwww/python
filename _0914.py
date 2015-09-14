#import module1

#coding:cp949
#인코딩 버전을 cp949로 하면 한글 출력 가능


#def sum_and_mul(a,b):
#    return a+b,a*b
#
#answer = sum_and_mul(10,30)
#print(answer)
ss="\t"

def printData(data,level=0):
    for item in data:
        if isinstance(item, list):
            printData(item,level+1)
                
        else:
            for ss in range(level):
              print("\t",end="")
            
            print(item)




data = ["홍길동",["베테랑",["류승완","황정민","유아인"],"암살",["최동훈","전지현","하정우"]],"고길동",["인사이드 아웃",["기쁨","슬픔"],"암살",["최동훈","전지현","하정우"]]]
module1.printData(data)
    

import os

help(os.getcwd())
#os.mkdir("Sample")
#os.chdir(".//sample")
#help(os.getcwd())