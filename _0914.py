#import module1

#coding:cp949
#���ڵ� ������ cp949�� �ϸ� �ѱ� ��� ����


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




data = ["ȫ�浿",["���׶�",["���¿�","Ȳ����","������"],"�ϻ�",["�ֵ���","������","������"]],"��浿",["�λ��̵� �ƿ�",["���","����"],"�ϻ�",["�ֵ���","������","������"]]]
module1.printData(data)
    

import os

help(os.getcwd())
#os.mkdir("Sample")
#os.chdir(".//sample")
#help(os.getcwd())