import pickle


fileName = "파일입출력예제1.txt"
fileName2 = "Monica.txt"
roles = []
roles2=[]
#with open(fileName, "w+") as myfile:
#    myfile.write("20101111 홍길동\n")
#    myfile.write("20101111 고길동\n")
#    myfile.write("20101111 김길동\n")
#    myfile.write("20101111 이길동\n")

with open(fileName, "r") as myfile, open(fileName2, "w") as monica:
    for content in myfile :
        (role, etc) = content.strip().split(":")
        roles.append(role)
pickle.dump(roles,monica)
    
with open(fileName2, "rb") as monica:
    result = pickle.load(monica)
