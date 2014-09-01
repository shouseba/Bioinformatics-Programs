#This program will open a file that is hard coded and
#calculate the Guanine/Cytosine content for the nucleotide sequence from
#FASTA (converted to .txt) files retrieved from the National Center for 
#Biotechnology Information website.
#Brandon Shouse

#Introduction
print("\n\n===============================================================================")
print("\n\t\tGuanine/CytosineGuanine/Cytosine Content Calculator\n")
print("===============================================================================")
print("This program will calculate the Guanine/Cytosine content based on the BRCA1\nHomo sapiens FASTA file retrieved from the NCBI website...")
print("\nThe file name and location are hard coded into the python script. To change\nthe file, please edit the python script to open the desired file.")
print("===============================================================================")

#Set the file to be opened
filename = "FASTA/BRCA1.txt"

#Open the file
geneSeq = open(filename, "r")
print("\nOpening file: " + "~/" + filename)

#Declare variables for each base pair and total base pair, initialize to 0
Guanine = 0;
Cytosine = 0;
Adenine = 0;
Thymine = 0;
totalBP = 0;

#Skip the first line of header in FASTA/TXT file
geneSeq.readline()

#Convert to lower case and get counts for each base pair. If g, c, a, or t is found, add one to the toalBP
for line in geneSeq:
	line = line.lower()
	for char in line:
		if char == "g":
			totalBP += 1
			Guanine += 1
		if char == "c":
			totalBP += 1
			Cytosine += 1
		if char == "t":
			totalBP += 1
			Thymine += 1
		if char == "a":
			totalBP += 1
			Adenine += 1
			
#Print the count for each base pair
print("\n\nResults of analysis: \n")
print("Total Base Pairs = " + str(totalBP))
print("Guanine Count = " + str(Guanine))
print("Cytosine Count = " + str(Cytosine))
print("Adenine Count = " + str(Adenine))
print("Thymine Count = " + str(Thymine))

#Calculate GC Content
gc = ((Guanine+Cytosine+0.) / (totalBP)) * 100
print("\nGuanine/Cytosine content: " + str("%.2f" %(gc))  + "%")