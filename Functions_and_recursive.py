### Use recursive function to generate the Fibonacci sequence

n=input("Give positive integer value: ")
n=int(n)
length=range(0,n+1)
###defining a function for recursive sequence
def function(n):
    '''if integer value(n)=0 then give 0 value,
        if integer value=1 then give 1 value,
        if it is >1 then use the formula Fn = Fn-1 + Fn-2 to calculate value for that integer.
    '''
    if n==0:
        return(0)
    elif n==1:
        return(1)
    elif n>1:
        return(function(n-1))+(function(n-2))

Fibonacci_sequence=map(lambda n:(function(n)),length)
print("Ans1: The fibonacci sequence for integer %s is %s"%(n,list(Fibonacci_sequence)))

######################################################################################################################################################################

# DNA compression and decompression,

#compression
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

###Decompression

###defining the function
def decom_string(givenstring):
    '''
    decompressing the given string by multiplying the alphabet by numerical value of repitition for that nucleotide
    '''
    ####initializing a variable to store decompressed nuleotide
    decompressed_string=""
    for i in given_string:
        ###if i in given string is alphabet then print i as nucleotide
        if (i.isalpha())==True:
            nucleotide= i
        ###if i in given string is numeric value then print i as numeric
        elif (i.isnumeric())==True:
            numeric=i
            ###then multiply the alphabet by numeric value for that nucleotide.
            decompressed_string=decompressed_string+nucleotide*int(numeric)
    return(decompressed_string)
given_string="A1C1A2G1A1T1G1C2A1T2G1T1C5G2C2T1C2T1G1C1T1"
decompressed=decom_string(given_string)
print("The given Dna string is %s and the decompressed string is %s"% (given_string , decompressed))

#####################################################################################################################################################################
###Pig latin encrypt and decrypt and shift cipher encrypt and decrypt
import re
import sys

'''
    Part A:Pig latin Encrypt and decrypt
    Part B: shift cipher encrypt and decrypt
'''
###part A:pig latin encrypt
def encrypt_pig_latin(statement):
    '''if starting letter is a vowel
        add 'ay' to the end of word
       if starting letter is not vowel
        move the starting letter to the end and add 'ay'
    '''
    encrypt_statement=""
    for word in statement.split(" "):   ###it will give you each word
    ##create a regix pattern to match word starting with vowel or not and if it match add 'ay'to the word at last
        pattern=re.compile(r'[aeiou]',re.I)
        if pattern.match(word):
            word=word+'ay'
    ####if the pattern doesnot match then take the 1st letter to last and add 'ay'
        else:
            word=word[1:]+word[0]+'ay'
        ###then append the word in sentence
        if (len(encrypt_statement)):
            encrypt_statement=encrypt_statement+" "+word
        else:
            encrypt_statement=word
    return(encrypt_statement)

statement=input("Type any sentence or word:")
print("Given statement is %s"%statement)
# print(statement)
encrypt_sen=(encrypt_pig_latin(statement))
print("The pig latin encryption sentence is: %s"% encrypt_sen)

####piglatin decrypt
'''
    accept pig latin encrypt statement
    give decrypt statement
'''
def piglatin_decrypt(sentence):
    '''
        word starting with non vowel letter
        remove 'ay'and place the 1st letter at first
        word starting with vowel letter
        remove 'way' from last leter of the word
    '''
    decrypt_statement=""
    for word in sentence.split(" "):
        ##create a regix pattern to match word starting with vowel or not and if it match remove 'ay'from the word and give the word
        pattern=re.compile(r'[aeiou]',re.I)
        if pattern.match(word):
            word=word[0:-2]
        ###else give the word by placing the last 3rd letter at first followed by other letter from position 1:-3 respectively.
        else:
            word=word[-3]+word[:(len(word)-3)]
        if (len(decrypt_statement)):
            decrypt_statement=decrypt_statement+" "+word
        else:
            decrypt_statement=word
    return(decrypt_statement)
sentence=encrypt_sen
print("The pig latin decryption sentence from the above encryption is: %s"% (piglatin_decrypt(sentence)))

#######################################################################################################################################################
###Part B:shift Cipher encrypt and decrypt
###encryption

def encryption_statement(statement,shift):
    '''
    shifting each letter in word of statement by given value of shift and replacing with shifted word
    '''
    encryption_shift=""
    for i in statement:
        ###look for lower case letter
        if i.islower():
            ###find the position of alphabet within range 0-25
            i_unicode=ord(i)
            i_place=ord(i)-ord("a")
            ###perform the shift
            new_place=(i_place+shift)%26+ord("a")
            ###convert to character
            new_letter=chr(new_place)
            ###append in new encrypted statement
            encryption_shift=encryption_shift+new_letter
        elif i.isupper():
            ###if it is in upper case repeat the upper case using uppercase alphabet
            i_unicode=ord(i)
            i_place=ord(i)-ord("A")
            new_place=(i_place+shift)%26+ord("A")
            new_letter=chr(new_place)
            encryption_shift=encryption_shift+new_letter
        else:
            ###if it is neither uppercase nor lowercase letter keep it as it is.
            encryption_shift+=i
    return(encryption_shift)
statement="hello all"
print("The given statement is %s"% statement)
shift=4
encryption=encryption_statement(statement,shift)
print("The encrypted statement is: %s after shifting the given statement by %s" %(encryption,shift))

###decryption:
def decryption_statement(statement,shift):
    '''
    shifting each letter in word of statement by given value of shift and replacing with shifted word
    '''
    decryption_shift=""
    for i in statement:
        ###look for lower case letter
        if i.islower():
            ###find the position of alphabet within range 0-25
            i_unicode1=ord(i)
            i_place1=ord(i)-ord("a")
            ###perform the shift i.e. in decryption decrease the position
            new_place1=(i_place1-shift)%26+ord("a")
            ###convert to character
            new_letter1=chr(new_place1)
            ###append in new decrypted statement
            decryption_shift=decryption_shift+new_letter1
        elif i.isupper():
            ###if it is in upper case repeat the upper case using uppercase alphabet
            i_unicode1=ord(i)
            i_place1=ord(i)-ord("A")
            new_place1=(i_place1-shift)%26+ord("A")
            new_letter1=chr(new_place1)
            decryption_shift=decryption_shift+new_letter1
        else:
            ###if it is neither uppercase nor lowercase letter keep it as it is.
            decryption_shift+=i
    return(decryption_shift)
statement1=encryption
print("The decrypted statement from the above encrypted statement is: %s after shifting by %s "% ((decryption_statement(statement1,shift)),shift))

#############################################################################################################################################################################

###finding the common motif.
'''
    finding common motif from fasta file sequences
'''
import re
###create a function to look at motif in each sequence
def look_motif(motif, lines_list):
    for sequence in lines_list:
        if not re.search(motif, sequence):
            ####if motif not present, returns null value
            return 0
        return motif ###if motif present returns the motif

#####opening the file,setting the minimum motif length as integer, and creating a file handle
file=open('contigs.fasta', "r+")
n=int(6)
lines_list=[]
string = ""
###read the line and find line starting with ">" and append it in string handle
for line in file.readlines():
    if re.search(r"^>",line):
        if string:
            lines_list.append(string +"\n")
        string = ""
    else:
        string += line.strip()
motif_list =[]
for n in range (n, len(lines_list[1])):
    possible_motifs =re.findall(r".{%i}" %(n),lines_list[1])
    for motif in possible_motifs:
        pattern=look_motif(motif, lines_list)
        if pattern:
            motif_list.append(pattern)
print("The conserved motifs are:", motif_list)
file.close()

###########################################################################################################################################################################################################
'''
    solving the arithmetic equation using regex
'''
numeric="8 + (9*-2) - 4 * 5/5="
import re
import sys
###search for "=" at the end of equation using regex and replace it with blank.
pattern=re.compile(r"\=")
match=pattern.findall(numeric)
for i in match:
    numeric=numeric.replace(i,"")
    print(numeric)
match2=re.findall(r'\/(?<!\.)\b0',numeric)
for i in match2:
    print("Error:Zero divisible Error")
    break
    if not match2:
        continue
###look for parenthesis and any number within that parenthesis which may or maynot have negative sign in front of number.Then replace it with evaluation of that number in main equation.
match=re.findall(r"(\(\-*\d*\.*\d+[+-/*]\-*\d*\.*\d+\))",numeric)
for i in match:
    numeric=numeric.replace(i, str(eval(i)))
###now look for operators like *,/,+,- within and solve parenthesis.Then replace the value in the main equation.
while True:
    match1=re.findall(r"(\d\.*\d*\s*\*\s*\-*\d*\.*\d)",numeric)
    if not match1:
        break
    numeric=numeric.replace(match1[0], str(eval(match1[0])))

while True:
    match1=re.findall(r"(\d\.*\d*\s*\/\s*\-*\d*\.*\d*)",numeric)
    if not match1:
        break
    numeric=numeric.replace(match1[0], str(eval(match1[0])))

while True:
    match1=re.findall(r"(\-*\d\.*\d*\s*\+\-*\s*\-*\d*\.*\d*)",numeric)
    if not match1:
        break
    numeric=numeric.replace(match1[0], str(eval(match1[0])))
while True:
    match1=re.findall(r"(\-*\d\.*\d*\s*\-\s*\-*\d*\.*\d*)",numeric)
    if not match1:
        break
    numeric=numeric.replace(match1[0], str(eval(match1[0])))
solved=float(numeric)
solved='%.3f' % solved
print("%s"% solved)

########################################################################################################################################################################################

'''
    Clean up the tweeter stream such at all URLs, hashtags, mentions, punctuations, RTs and CCs and removed and only the user’s message remains.
    E.g: Input = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
    Output = 'Good advice What I would do differently if I was learning to code today'
'''

input='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt @ramesh #rstats'''
import re
###searching for a pattern using regex and finding them all.For each matched regix word replace it with empty space.Then print the sentence.
pattern=re.compile(r'http:\/\/[.\w\/]*|cc:[\s*\@\w+]+|\#[\w]*|\w*\s*\(*\@[\w*:]*\)*|[\!*\~*\**\$*\+*\-*]')
match_pattern=pattern.findall(input)
print(match_pattern)
for m in match_pattern:
    input=input.replace(m,"")
print("%s" %input)
