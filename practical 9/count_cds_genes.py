fhand = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') #open the file
seq = "" #identify the seq as the string
end_codes= input("please choose a endcode from TAA,TAG,TGA: ") #use an input to let somebody print the end code
for line in fhand: #read the file line by line
    if line.startswith('>'): #it shows this is the title line
        title =line.split(" ")[0] #get the title and put it into the "title"
        if seq.endswith(end_codes): #to find the sequence that endswith end_codes
            new_file= open(end_codes+'_stop_genes.fa','a') #creat a new file to sort the result
            number="  the number of coding sequences is :"+str(seq.count(end_codes)) #the	number	of	coding	sequences	made	in	 this	gene	using	 the	given	stop	codon
            title=title+number
            new_file.write(f'{title}\n{seq}\n') #write the gene sequence
            new_file.close
            seq = "" #clear the sequence so that it can sort new gene
    else:
        seq=seq+line.strip('\n')

