###Decompression of a DNA string
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