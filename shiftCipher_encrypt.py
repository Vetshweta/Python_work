###shift Cipher encrypt
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