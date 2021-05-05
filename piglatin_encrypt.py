###Pig latin encrypt
import re
import sys

'''
    Pig latin Encrypt
'''
###pig latin encrypt
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