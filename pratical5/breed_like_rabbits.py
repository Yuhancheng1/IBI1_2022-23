# n means the total	number of rabbits that will be born each generation,m means the number of whole rabbits,j means the rabbit generation
j=1;n=0;m=2
while m<100:
    j=j+1
    n=m
    m=m+n
print(str(j),str(m))
#the result show in the 7 generation, there will be total 128 rabitts
