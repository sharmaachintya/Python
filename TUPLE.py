Month=("January","February","March","April","May","June","July","August","September","October","November","December")
Bday=input("Enter your Birthday (DD-MM-YYYY) :")
index=int(Bday[3:5])-1
bd=Month[index] 
print("You were born in ",bd)