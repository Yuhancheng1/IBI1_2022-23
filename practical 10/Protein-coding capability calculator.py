import re
total_DNA1="acgcaATGtgccgaataatattagcgttaatagccTGAattcag"
total_DNA1=total_DNA1.upper() #Integrate the initial sequence as a whole
total_DNA=re.findall('ATG.+?TGA',total_DNA1) #Use re. findall to extract the sequence starting with ATG and ending with TGA from the gene sequence
total_DNA="".join([str(x) for x in total_DNA]) #Convert the extracted list type to str
DNA_sequence = input("please enter a DNA sequence instead of ATG or TGA: ")
DNA_sequence=DNA_sequence.upper() #Unify gene sequences in uppercase
def check(a,b) : #Define the function check, which has two parameters, a and b, where a represents the total gene sequence and b represents the given gene sequence for detection
    m=1
    n=0
    i=len(b)
    j=len(a)
    k=j-6  #M represents the marker used to intercept strings, n represents the number of genes that meet the standard, and k represents the length of the total gene sequence without the promoter and terminator
    if k/3!=k//3 : #Determine if this code is a multiple of three. If it is not, it indicates that it is uncoded because the codons are paired with three
        print("this is non-coding")
    else :
        while m + i <= k + 3 - i:  # This condition indicates that a gene sequence of appropriate length can also be obtained from the total DNA
            s1 = a[m + 2:m + i + 2:1]  # The gene sequence with length j was intercepted and stored in s1
            if s1 == b:
                n += i  # If the intercepted sequence has the same length as the given sequence, then the length of the sequence is accumulated and modified on n
            m += i  # Continue searching backwards in groups of three gene sequences to avoid duplicate searches
        if n / k > 0.5:
            print("this is a protein-coding")
        elif n / k < 0.1:
            print("this is non-coding")
        else:
            print("this is unclear")  # Detect gene sequences according to three testing standards
check(total_DNA, DNA_sequence)  # call the funtion
