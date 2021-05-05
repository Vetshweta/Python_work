###shift Cipher decrypt
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