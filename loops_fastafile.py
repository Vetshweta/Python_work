####finding hamming distance:
#The Hamming distance between two string of same length is the minimum number of substitutions required to transform one string into the other

string1="ATTTCCGAG"
string2="ATGCGTAGT"
def hamming_distance(string1,string2): ###creating a definition function for hamming_distance.
    distance=0
    l=len(string1)
    for l in range(l):
        if string1[l]!=string2[l]:
            distance+= 1
    return distance
print(hamming_distance(string1,string2))

##############################################################################################################################################################

###Pretty print FASTA file where DNA sequence on each line has no more than 80 nucleotides

###creating a variable name fasta_file which contain fasta sequence and opens it.
fasta_file=open("contigs.fasta","r")
linenum=0
for line in fasta_file:
    line_stripped=line.rstrip() ###removing white space
    length=len(line_stripped)
    if ((length>80)and (line[0]!=">")):
        position=range(0,length,81)
        for i in position:
            line_stripped=line_stripped[:i]+"\n"+line_stripped[i:]
    print(line_stripped)
############################################################################################################################################################

###Convert a FASTQ file to FASTA file format

###openning fastq file and creating fasta_out.txt file for storing result output.
fastq_file=open("fastq_sample.fasta","r+")
fasta_out=open("fasta_out.txt", "a")
count=0
for line in fastq_file:
    count+=1
    if count==1:
        line1=">"+line[1:]
        fasta_out.write(line1)
#        print(line1)
    if count==2:
#        print(line)
        pos=range(0, len(line),81)
        for i in pos:
            line2=line[:i]+"\n"+line[i:]
        fasta_out.write(line2)
    if count==4:
        count=0
fasta_out.close()
f=open("fasta_out.txt", "r+")
for line in f:
    print(line)

#################################################################################################################################################################

###Given a FASTQ file, and quality cut-off value q and min sequence length n (assume Phred33 quality score).  Trimmed from the both ends (removed leading and trailing bases with quality lower than q), only report reads with min length of n (remove all reads with length less than n)

###creating phred dictionary
phred_dict = {'!':0, '"' :1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8,\
 '*':9, '+':10, ',':11, '-':12, '.':13, '/':14, '0':15, '1':16, '2':17, \
     '3':18, '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, \
         ';':26, '<':27, '=':28, '>':29, '?':30, '@':31, 'A':32, 'B':33,\
              'C':34, 'D':35, 'E':36, 'F':37, 'G':38, 'H':39, 'I':40, 'J':41, 'K':42}

fastq_file=open("fastq_sample.fasta","r+")
cutoffoutput=open("cutoffoutput.fasta","a+")
count=0
quality_cutvalue=36
minimum_length=35
for line in fastq_file:
    count+=1
    if count==1:
        line1=line
        continue
    if count==2:
        seq = line
        continue
    if count==3:
        line3=line
        continue
    if count==4:
        quality=line.rstrip()
        frontcut=-1
        for x in quality:
            frontcut+=1
            qualitycut=phred_dict.get(x)
            if qualitycut >= quality_cutvalue:
                break
        reverse_quality=quality[:: -1]
        reversecut=-1
        for y in reverse_quality:
            reversecut+=1
            quality_value=phred_dict.get(y)
            if quality_value>=quality_cutvalue:
                break
        if len(quality[frontcut: len(quality)-reversecut]) > minimum_length: ##if quality length is more then the minimum length write the sequence on the cutoffoutput file
            cutoffoutput.write(line1)
            cutoffoutput.write(seq[frontcut: len(quality)-reversecut]+"\n") ###trimming the sequence based on front and back cut off points
            cutoffoutput.write(line3)
            cutoffoutput.write(quality[frontcut: len(quality)-reversecut]+"\n") ###trimming the quality based on the front and back cut off points
        count=0
        print(frontcut, reversecut)   ##checking the cut off points to validity purpose
cutoffoutput.close()
final_outfile=open("cutoffoutput.fasta","r+")   ###printing the output file
for line in final_outfile:
    print (line)

#######################################################################################################################################################################


###Given a FASTQ file and a threshold Print all sequences where average read quality is below the threshold and Print all sequences where average read quality is at least the threshold

###creating phred dictionary
phred_dict = {'!':0, '"' :1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8,\
 '*':9, '+':10, ',':11, '-':12, '.':13, '/':14, '0':15, '1':16, '2':17, \
     '3':18, '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, \
         ';':26, '<':27, '=':28, '>':29, '?':30, '@':31, 'A':32, 'B':33,\
              'C':34, 'D':35, 'E':36, 'F':37, 'G':38, 'H':39, 'I':40, 'J':41, 'K':42}
###fixing threshold at 38
threshold= 38
###import fasta_file
###create two variable named fastq_methreshold and fastq_belowthreshold to write output of sequence which meets given threshhold and below threshold respectively.
fastqfile=open("fastq_sample.fasta","r+")
fastq_methreshold=open("fastq_methreshold.txt", "a")
fastq_belowthreshold=open("fastq_belowthreshold.txt", "a")
count=0
for line in fastqfile:
    count+=1
    if count==1:
        line1=line
    if count==2:
        line2=line
    if count==3:
        line3=line
    if count==4:
        line4=line.rstrip()
        quality=[]
        for x in line4:
            quality_phred=phred_dict.get(x)
            quality.append(quality_phred)
            import math
        average_quality=sum(quality)/len(quality)
        #print(average_quality)
        if average_quality>= threshold:
            fastq_methreshold.write(line1)
            fastq_methreshold.write(line2)
            fastq_methreshold.write(line3)
            fastq_methreshold.write(line4 +'\n')
        else:
            fastq_belowthreshold.write(line1)
            fastq_belowthreshold.write(line2)
            fastq_belowthreshold.write(line3)
            fastq_belowthreshold.write(line4+'\n')
        count=0
fastq_methreshold.close()
fastq_belowthreshold.close()

#########################################################################################################################################################################

#####Find the longest repeat in the string S, if multiple solutions exists print all solutions.  A "repeat" is a substring of S that does not have to be same character repeating consecutively 

##given a test string
test_str ="TGTCAGCTACCTTGATGGATTGAGTTTGTTTCGGTCGATGCTCCATCGGGAGAG\
AGTCTGCGTCCTGGTCCGAGCAAGTCCCACCAAGTGGCACTTGGCGGCGCCATGTCCTAT\
CTAGTGCCACCATGTCCGAGGACTTTGATGGCACATGGTGGCACTTGATTTGCCCAAGTCCCACCT\
GCTCCGACGTGGACCGACTTCGTGGCACATCGCTATCACCCACTCTACCGTTGAAAAGCC\
GAAGTCAAGCGCCGAAAGCTGATCGATTTGCGGTGTGATACGTTGCCAGTGATTCGTTCC\
GTGGTTTATGCTTGGCGCACCTACCGCGTCCCCGACGCATCGACTCCGCCGCCATTGCGC\
GGCACAAAACGGCCTTCGATCCTTCCGTACGGAGGGGTACTGCAGGGCTCACTGTTCATG\
CCGGAAATTGCACCGGCTTTTTTTTCAATCAAATCAAGTGGACCGTGTCGGATAGTGAGG\
ACACCGGACACCGCGATACCAAGCCGATTGGCGGTCTGTTTGTGAAAATAGACCGTAGTG\
CGGACAATTCCGAAGCCGGACACCGGACAGGTGCTCTGTGGAAATTCCGCGTATGCCCGA\
CACCCTTACAGCCGCGTGGCTGGGTGCGGATCACGAAGCCCAAAACACTGCGGCGGGGAT\
GATCTGACTTTGGGGTGGGGAGCTGCTTTGCGTGCCGAATGACGGCGAACGCAGGCTTCT\
GAGCAAATATCGATCCGGGGGGCGCCACCGGTACCAGAACGGCGCAACAGGTAATCACCC\
ATCACGGCAAGGGCCGCAGGCGTGTGGACGCAATCCACGCGAAGGCAGGCTCGCATCCAG\
AGATGCACCGGATAGGGTGGCCGCGCAAGCGGTGCGTGAGGCGAGAGCCTTGCATGTTCG\
CGAAGCGGACGGTCACGACGCATTGCTTCCATGCTCAGGGCCGATCGGTTTGGCATCGCT\
AAAGGACCGGAAGAGTGGTTGTAGGACCGGCAGGGTGGGCCGGCAAGCTGGGGGTGGTAC\
CCCGGTGCACCAAGCGGGCAGGGCCAATTCGGGGTTGGCGCCGCCGAGAATTGGGTTGCG\
CAGATTTGCGCGGCCGGCGGGATGCGCTTAGCGCGAATAGGAATCCGTC"

###creating a function to determine longest common string
def longest_repeat(a, b):
  n = min(len(a),len(b))
  for x in range(0,n):
    if(a[x] != b[x]):
      return a[0:x]
  else:
    return a[0:n]

longest_sequence ="" ####creating a place holder for longest string
n = len(test_str)
for i in range(0,n):
  for j in range(i+1,n):
    z = longest_repeat(test_str[i:n],test_str[j:n])
    if(len(z) > len(longest_sequence)):  ### if new string is largest than previous then takes the new long string.
      longest_sequence=z
print("Longest repeating sequence:%s"%longest_sequence)

####################################################################################################################################################################

###Ask the user for a string and print out whether this string is a palindrome or not.

string=input("Enter string:")
reverse_string="".join(list(string[: :-1]))
if string == reverse_string:
    print("It is palindrome")
else:
    print("Not palindrome")

##########################################################################################################################################################################

###Guessing game, generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
guess_number=input("Select number between 1-9: " )
guess_number1=int(guess_number)
print("Answer 8:guessed number is %s"% guess_number1)
import random
random_selection=random.randint(1,9)
print("random selected number is %s" %random_selection)
if guess_number1 > random_selection:
    print("guessed too high")
elif guess_number1<random_selection:
    print("guessed too low")
elif guess_number1==random_selection:
    print("guessed exactly right")


##############################################################################################################################################################################

###Given a RNA string, print protein encoding by it. Use following RNA codon (https://en.wikipedia.org/wiki/Genetic_code#RNA_codon_table (Links to an external site.)) table to translate your RNA string

RNA_string="AUGCAUGCAGC"
##creating a RNA codon dictionary
codon_dict={"UUU":"F","CUU": "L", "AUU": "I", "GUU":"V", "UUC":"F", "CUC":"L", "AUC": "I", "GUC":"V",
            "UUA": "L", "CUA": "L", "AUA":"I" ,"GUA":"V", "UUG":"L" ,"CUG": "L" ,"AUG":"M" ,"GUG": "V",
            "UCU":"S" , "CCU":"P", "ACU":"T", "GCU":"A","UCC":"S" ,"CCC":"P", "ACC":"T" ,"GCC":"A",
            "UCA":"S" ,"CCA":"P" ,"ACA":"T" ,"GCA":"A", "UCG":"S", "CCG":"P" ,"ACG":"T","GCG":"A",
            "UAU":"Y" ,"CAU":"H" ,"AAU":"N" ,"GAU":"D", "UAC": "Y", "CAC":"H" ,"AAC":"N" ,"GAC":"D",
            "UAA": "Stop", "CAA":"Q" , "AAA":"K" , "GAA":"E", "UAG":"Stop" , "CAG":"Q" , "AAG":"K" ,"GAG":"E",
            "UGU":"C" ,"CGU": "R","AGU":"S", "GGU":"G","UGC":"C" ,"CGC": "R" ,"AGC":"S" ,"GGC":"G",
            "UGA": "Stop","CGA":"R" ,"AGA":"R" ,"GGA":"G","UGG":"W","CGG":"R","AGG": "R" ,"GGG":"G" }
protein=""
for i in range(0,len(RNA_string), 3):
    codon=RNA_string[i:i+3]
    if len(codon) <3:
        break
    protein+=codon_dict[codon]
print("RNA string is:", RNA_string," and the corresponding protein sequence is:", protein)

##############################################################################################################################################################################