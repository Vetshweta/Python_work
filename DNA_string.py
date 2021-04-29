###DNA string is given 
###a)finding first and last stop codon, b)split from stop codon and reporting each fragment length and c)finding length of original DNA string, percentage of GC and count A,T,G,and C in the string.
DNA_string="CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC"
####first and last location of stop codon TAG
TAG1=DNA_string.find("TAG")
print("3.a ans. First location of TAG in given DNA string is :%s"%(TAG1))
TAG2_location=DNA_string.find("TAG", TAG1 +1 )
TAG3_location=DNA_string.find("TAG", TAG2_location +1 )
print("Last location of TAG in given DNA string is :%s" %(TAG3_location))

####Splitting the DNA string by stop codon TAG and reporting each fragment and their respective lengths
fragments=DNA_string.split("TAG")
print("The 1st fragment of DNA string splitted by stop codon TAG is: %s and its length is: %s" % (fragments[0], len(fragments[0])))
print("The 2nd fragment of DNA string splitted by stop codon TAG is: %s and its length is: %s" % (fragments[1], len(fragments[1])))
print("The 3rd fragment of DNA string splitted by stop codon TAG is: %s and its length is: %s" % (fragments[2], len(fragments[2])))
print("The 4th fragment of DNA string splitted by stop codon TAG is: %s and its length is: %s" % (fragments[3], len(fragments[3])))

####length of original DNA string
print( "The length of original DNA string S is: %s"%len(DNA_string))
####percentage of GC in original DNA string
print("Percentage of GC in original DNA string is: %s" %((DNA_string.count("GC")/len(DNA_string))*100))
####Report number of A, C, T and G's
print("The number of A,C,T,G in DNA string is: %s, %s, %s, %s respectivly."% (DNA_string.count("A"),DNA_string.count("C"),DNA_string.count("T"),DNA_string.count("G")))

#############################################################################################################################################################################################################################################################################

##In a DNA , 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a DNA string S create a reverse complement (e.g: reverse complement of "GTCA" is "TGAC").
string="ATGCATCGTCGAC"
reverse=string[: :-1]
complement = {'A':'T','G':'C','T':'A','C':'G'}
print("Ans:2: The reverse complement of string %s is %s"%(string, "".join(complement[x] for x in list(reverse))))