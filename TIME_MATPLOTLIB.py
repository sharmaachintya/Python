import matplotlib.pyplot as plt
import time as t
word="apple"
mistake=0
lst=[]
print("The word is apple ")
input("Press ENTER to continue")
for i in range (0,5):
    start=t.time()
    wo=input("Enter the word: ")
    end=t.time()
    time_taken=end-start
    lst.append(time_taken)
    if wo != "apple":
        mistake=mistake+1
print("You made " + str(mistake) + " Mistakes")
print("YOUR EVALUATION")
t.sleep(3)
att=[1,2,3,4,5]
plt.plot(att,lst)
plt.show()