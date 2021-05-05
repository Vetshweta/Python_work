#DNA compression
DNA_string="ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCG"
compressed_string=""
count=1
for i in range(0,len(DNA_string)):
    if i==0:
        nucleotide=DNA_string[i]
        continue
        print(nucleotide)
    elif DNA_string[i]==DNA_string[i-1]:
        count+=1
        if i ==len(DNA_string)-1:
            compressed_string+=nucleotide+str(count)
    else:
        compressed_string+=nucleotide+str(count)
        nucleotide=DNA_string[i]
        count=1
        if i==len(DNA_string)-1:
            compressed_string+=nucleotide+str(count)
print("The given Dna string is %s and its compressed string is %s" % (DNA_string,compressed_string))