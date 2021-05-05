###Convert a FASTQ file to FASTA file format each line length of 80 nucleotide

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