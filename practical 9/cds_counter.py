import re
seq ='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
result_1=re.findall(r'^ATG.+?TGA', seq) #use re.findall to find a list that whose head is ATG and tail is TGA
result_2=re.findall(r'^ATG.+?TAA', seq) #use re.findall to find a list that whose head is ATG and tail is TAA
count=len(result_1)+len(result_2) #use len() to count the number of lists and add them all
print (count)
