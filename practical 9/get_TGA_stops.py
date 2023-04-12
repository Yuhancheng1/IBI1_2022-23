fhand = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
n=0 #define n as a timer to counte the gene that end with TGA

for line in fhand: #check the file line by line to find whether it is the title line or the gene line
    if line.startswith ('>'): #it shows this is the title line
        title = line.split(" ")[0] #get the title and put it into the "title"
        if n!=0: #Prevent errors from being reported during the first run due to undefined 'seq'
            if seq.endswith('TGA\n'): #Find the gene sequence ending in TGA that meets the requirement.
               new_file= open ('TGA_genes.fa','a') #write a new flie named 'TGA_genes.fa',open it as approach model
               new_file.write(f'{title}\n{seq}') # Input gene names and corresponding gene sequences
               new_file.close
        n += 1
        seq = ""
    else:
        seq=seq+line #Temporarily storing gene sequences in seq
