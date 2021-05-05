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
print("The pig latin decryption sentence is: %s"% (piglatin_decrypt(sentence)))