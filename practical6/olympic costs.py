#make a list to store the cost of Olympic, called coats
#make coats list in order and store it into a new list called sorted_coats
#print the sorted_coats
coats=[1,8,15,7,5,14,43,40]
sorted_coats=sorted(coats)
print(sorted_coats)
#make the city date into the list cities
#Convert it to a numpy array. Sort the sorted cost list_ Coats are also converted to a numpy array and the argsort method is used to return a list of indexes sorted by cost. Then, use this index list to rearrange cities and sorted_ Arrays of coats, aligning them with corresponding cities and costs sorted by cost
cities=["Los Angeles 1984","Seoul 1988","Barcelona 1992","Atlanta 1996","Sydney 2000","Athens 2003","Beijing 2008","London 2012"]
import numpy
cities=numpy.array(cities)
costs=numpy.array(sorted_coats)
sortedcosts=costs.argsort()
sorted_cities=cities[sortedcosts]
sorted_costs=costs[sortedcosts]
#Create a bar chart
import numpy as np
import matplotlib.pyplot as plt
plt.xlabel("Cities")
plt.ylabel("Costs")
plt.title("Olympic Games Costs")
plt.bar(sorted_cities,sorted_costs)
plt.show()
