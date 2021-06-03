lst=["Pablo","Tenu","Buggu","Jamal"]
name=input("Enter your name : ")
if name not in lst:
    lst.append(name)
    print(lst)
elif name in lst:
    print("Name Alrady in list")