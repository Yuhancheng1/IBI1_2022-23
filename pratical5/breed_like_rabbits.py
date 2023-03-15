# n means the total	number of rabbits that will be born each generation,m means the number of whole rabbits,j means the rabbit generation，we use a while loop so that when the number of rabbits over 100 we can find it。
j=1;n=0;m=2
while m<100:
    j=j+1  
    n=m    
    m=m+n
print(str(j),str(m))
#the result show in the 7 generation, there will be total 128 rabitts
