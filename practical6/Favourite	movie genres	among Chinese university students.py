#First, we need to create a dictionary to store the students' favorite genes
favourite_genres={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
# Extract pie chart data and labels
import matplotlib.pyplot as plt
labels ='Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes = [73,42,38,28,22,19,28,12,8,7]
# creat a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# show the pie chart
plt.show()
#Enter a specific movie type and the number of students who like this type most will be output,and we show this in example comedy
favoriate='Comedy'
print(favourite_genres[favoriate])
