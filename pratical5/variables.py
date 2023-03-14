# a is the longitude of Edinburgh 
#b is the longitude of  Los Angeles
#c is the longitude of Haining
#d is the longitude difference	between	a and b	
#e is the longitude difference	between	a and c
a=-3.19
b=-118.24
c=116.39
d=a-b
e=c-a
if d>e:
        print("e is better")
elif e>d:
        print("d is better")
else:
        print("d is same to e")
# so Rob travel to Haining is further than to Los Angeles

X=True
Y=False
W=X and Y
Z=X or Y
print (W,Z)
#W means Flause,and Z means True
