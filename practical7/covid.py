#Introducing OS and Pandas databases
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#The code for importing the .csv file works
os.chdir("C:\\Users\\YHC16\\Desktop\\临时文件")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:1001:100,1]) #showing the second column from every 100th row from the first 1000 rows (inclusive).
#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
covid_data['the_afghanistan'] = (covid_data['location'] == 'Afghanistan')
print(covid_data.loc[covid_data['the_afghanistan'] == True,"total_cases"])
#Extract the data, location, new case, and new death from 2020-3-31 to new_data
covid_data['the_2020-3-31'] = (covid_data['date'] == '2020-03-31')
new_data=covid_data.loc[covid_data['the_2020-3-31'] == True,["new_cases","new_deaths"]]
newcases=new_data.iloc[0:195,0]
newdeaths=new_data.iloc[0:195,1]
print(new_data)
#Take new_cases and new_deaths from new_data, calculate their average value using numpy, and output
cases_mean=np.mean(newcases)
print(cases_mean)
deaths_mean=np.mean(newdeaths)
print(deaths_mean) #computed the mean number of new cases and new deaths on 31 March 2020.
newcases.plot.box(title="new cases")
plt.show()
newdeaths.plot.box(title="new deaths")
plt.show() #created boxplot of new cases and new deaths on 31 March 2020.
worlddates=covid_data.iloc[:,0]
worldcases=covid_data.iloc[:,2]
worlddeaths=covid_data.iloc[:,3]
plt.plot(worlddates,worlddeaths,'r+')
plt.xticks(worlddates.iloc[0:len(worlddates):4],rotation=-90,fontsize=4)
plt.show()
plt.plot(worlddates,worldcases,'r+')
plt.xticks(worlddates.iloc[0:len(worlddates):4],rotation=-90,fontsize=4)
plt.show()  #plotted both new cases and new deaths worldwide over time.

#uesd to answer the question that I asked
covid_data['the_Canada'] = (covid_data['location'] == 'Canada')
Canada_newcases=(covid_data.loc[covid_data['the_Canada'] == True,"new_cases"])
covid_data['Canadadate'] = (covid_data['location'] == 'Canada')
dates=(covid_data.loc[covid_data['the_Canada'] == True,"date"])
plt.plot(dates,Canada_newcases,'r+')
plt.xticks(dates.iloc[0:len(dates):4],rotation=-90,fontsize=4)
plt.show()
