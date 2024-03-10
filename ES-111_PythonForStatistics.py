import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt
#actual code 
def freq(list):
    freqs=[0]*10
    taken=set()
    for i in range(10):
        for j in range(10):
            if list[i]==list[j] and i not in taken:
                if(i!=j):
                     taken.add(j)
                freqs[i]+=1    
    return [item for item in freqs if item != 0]
def unique(list):
    newlist=[10]*10
    count=0
    taken =set()
    for i in range(10):
        if list[i] not in taken:
            newlist[count]=list[i]
            taken.add(list[i])
            count+=1
    return [item for item in newlist if item != 10]
list = [random.randint(0, 9) for _ in range(10)]#creat a list of 10 random integers
def sort(list):
    for i in range(10):
        for j in range(10):
            if(list[j]<list[i]):
                temp=list[j]
                list[j]=list[i]
                list[i]=temp
    return list
print("Data : ",end="")#print data
for _ in list :
    print(_,end=",")
print("")#print stats
print(f"Mode : {statistics.mode(list)}")
print(f"Mean : {pd.Series(list).mean()}")
print(f"Median : {pd.Series(list).median()}")
fig, (ax1, ax2,ax3) = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))
ax1.hist(list,bins=range(min(list),max(list)+2),color='skyblue',edgecolor='black')
ax2.scatter(unique(list), freq(list), marker='o', linestyle='-', color='b', label='Data')
ax3.plot(unique(sort(list)), freq(sort(list)), marker='o', linestyle='-', color='b', label='Data')
plt.tight_layout()
plt.sho
