#2023601 Rayyan Hassan Salman
#folloring is the code of ES-111 Project Python-For-Statistics

#import libruaries
import pandas as pd
import matplotlib.pyplot as plt
import random

#read te column "Marks Of Es 111 Students " from csv file to variable 'marks'
marks=pd.read_csv(r'Data.csv')['Marks Of ES 111 Students ']

#fetching the uniwue values and frequencies of those unique values in data
marks_frequency = marks.value_counts().sort_index() 
#marks_frequency.index ---> unique values
#marks_frequency.values --> Frequencies

#print out Basic Statistics
print(f"Mode :\n{marks.mode()}")
print(f"Mean :{marks.mean()}")
print(f"Median :{marks.median()}")
print(f"Range : {max(marks)-min(marks)}")
print(f"Standard Deviation :{marks.std()}")
print(f"Variance :{marks.var()}")
print(f"CoVariance :{marks.cov(marks)}")#i dont know which other dataSet to use to find covarience
print(f"Here is a random number x {{1<=x<=99 : {random.randint(1,99)}")

# Creating figure subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plotting line chart
axs[0,0].plot(marks_frequency.index, marks_frequency.values,marker="o", linestyle='-')#settings for accurate display
axs[0,0].set_title('Line Chart & Scatter Plot')     #Labels
axs[0,0].set_xlabel('Marks')
axs[0,0].set_ylabel('Frequency')

# Plotting histogram
axs[0,1].hist(marks, bins=range(min(marks),max(marks)+1), color='skyblue', edgecolor='black')#settings for accurate display
axs[0,1].set_title('Histogram')      #Labels
axs[0,1].set_xlabel('Marks')
axs[0,1].set_ylabel('Frequency')

#plotting bar chart
axs[1,0].bar(marks_frequency.index, marks_frequency.values, color='skyblue')#settings for accurate display
axs[1,0].set_xlabel('Marks')        #Labels
axs[1,0].set_ylabel('Frequency')
axs[1,0].set_title('Bar Chart')

#making pie chart
axs[1,1].pie(marks_frequency.values,labels=marks_frequency.index, autopct='%1.1f%%', startangle=90)#settings for accurate display
axs[1,1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
axs[1,1].set_title('Pie Chart') #Labels
 
# Adjust layout
plt.gcf().canvas.manager.set_window_title('Graphs')#set title of window to charts
plt.tight_layout()#to prevent overlpping of charts 
plt.show()#display charts