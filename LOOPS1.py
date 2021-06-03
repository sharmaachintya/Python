import random
names=[]
for i in range(0,8):
    name=input("Enter Name : ")
    names.append(name)
print(names)
n=random.randint(0,7)
pers=names[n]
print("Random Person ",pers)