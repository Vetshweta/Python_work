#####Write a regular expression to extract and validate an email address from input.  Validate traditional email addresses such as .com, .net, .org etc or country specific email address such as .co.uk or .co.in or .co.au etc
emailadress=["jaysheel@udel.edu", "jaysheel@dbi.udel.edu", "jaysheel@google.com", "jaysheel.bhavsar@domain.co.au", "jaysheel_bhavsar@subdomain.domain.net", "jaysheel@goog.co", "jaysheel@extension", "jaysheel-bhavsar@domain.ext"]
import re
pattern= re.compile(r'(\w+\S+)*@([\w+\S]*)\.(\w+)')
for email in emailadress:
    print(pattern.findall(email))

##################################################################################################################################################################################################################################################
   
####Write a program that takes a chemical formula as an input and outputs the number of each element's atoms.
####example Fe2(SO4)3

formula='Fe2(SO4)3'
import re
pattern1 =re.compile(r'\(\w+\)\d+')
m1=pattern1.findall(formula)
if (len(m1)>0):
    for i in m1:
        pattern2 = re.compile(r'\((\w+\d+)\)(\d+)')
        replace_with1 = pattern2.findall(i)[0][0]*int(pattern2.findall(i)[0][1])
        replace_formula1 = formula.replace(i, replace_with1)
else:
        replace_formula1 = formula
pattern3= re.compile(r"[A-z][a-z]*\d+")
m2=pattern3.findall(replace_formula1)
for i in m2:
    pattern4 = re.compile(r'([A-Z][a-z]*)(\d+)')
    replace_with2 = pattern4.findall(i)[0][0]*int(pattern4.findall(i)[0][1])
    replace_formula1 = replace_formula1.replace(i, replace_with2)
pattern5=re.compile(r"[A-Z][a-z]*")
m3= pattern5.findall(replace_formula1)

dictionary={}
for m in m3:
    if m in dictionary:
        dictionary[m]=dictionary[m]+1
    else:
        dictionary[m]=1
print(dictionary)

##########################################################################################################################################################
####Retrieve all the words starting with ‘p’ or ‘P’ from the input file.
####Content of an example input files:
     #Peter Piper picked a peck of pickled peppers.
     #Did Peter Piper pick a peck of pickled peppers?
     #If Peter Piper picked a peck of pickled peppers,
     #where's the peck of pickled peppers Peter Piper picked?
     
input_file = open('text.file.txt','r')
import re
m=re.compile(r'[pP]+\w+')
for line in input_file:
    p_word=re.findall(m,line)
    for word in p_word:
        print(word)
print("Ans5: List of all word startig with 'P' or 'p' are %s" %(word))

############################################################################################################################################################################
##Given a DNA string P and a contig C
#a)finding the reverse compliment of P in C, and printing its starting location
#b)find all occurrence of P in C, and print any and all starting locationsOccurance of P in C

P = "CTTAAAAGCG"
C="CGCTTTTAAGACTTAAAAGCGTTTGCTATGGACCTTAAAAGCGATCCACTTAAAAGCGTCTTAAAAGCGAACTTAAAAGCGGCGATTTGTCCTGCCTGAGTGCGGAATCAGAGGTTGATGTGTTGATGGACTCGAGTCATACAAGCGGAACTAGATACGGGGGGACTTCACCTGCGTTCTCAACTGCAGATCTAGAAGTGTTGATGTAGCTAGCACTCCAGAACGACTGTTTAACTTGGAGACCTCTCGTACAACATTTCGTTTCCGACACCCGTGTATAGGCGTCAAGAACGGAACCCGTATCTTAGAGGGGGATTCTCTTTTCTTACTCAAATTTGTGGCGGAATAACCGCGAATGAATCAACTGTATGCGGCTCTACTATGTGTAGATCATTTCGCATCAGCACCCAGAGCGCCCAGTGCAATACTGGTTGCCAGTTGCGCTGTATCCTTGACCCAGATGATAGTCCTAGGATCTAGGCCCGCGCAAACACCCCTAGTTATCCCAACATTCGCCGCCAAAAGGGTCAACAAGAGCGGGGCTGGAACTTCATCGCTTTTGCTATGAGGTTAAAACATCGGTACAGAGAACCCCCGGTGCAGGGAGGGGATGGGTATTGGGAACAAGATATACGAGCCGGAGCAAAGCGTCATTACCCATGTGTAGGAACACGGGGTTCAAAGTAGTCCACAATCCACGATCGATTCCCATGAACCTGGCCATATGAGCCAAGTCGTACTATAAGAAGCCTCTCCGCGCCTACGCCGCACGTTTTAAGGCCGTTTATCTTCCGTGATACTGGGTCGGTGTGC"
import re
reverse_P=P[: :-1]
complement_base={'A':'T','G':'C','T':'A','C':'G'}
reverse_complement=print("Reverse complement of P is %s "% ("".join(complement_base[x] for x in list(reverse_P))))
start_location=print("Starting location of reverse complement of P in C is %s" %C.find("CGCTTTTAAG"))

#finding occurence of P in C
pattern=re.findall(r'CTTAAAAGCG',C)
print(pattern)
occurance_count= print("Total number of occurance of P in C is %s"%C.count(P))

# starting location of occurance of P in C.
match=re.finditer(r'CTTAAAAGCG',C)
for m in re.finditer('CTTAAAAGCG',C):
    print(m.span()[0])
print("Starting location of 1st,2nd, 3rd, 4th and 5th P string in C contig is 11,33,48,59,71 respectively.")
     
##########################################################################################################################################################################