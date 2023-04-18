ccno = '1347-1067-4839-4562'
 #defieing the functions 
def hideccno(ccno):
    strng = '' #empty string
    if len(ccno) > 4:
        strng += '*' *(len(ccno) - 4)+ccno[-4:] #here we are slicing the strings to just blur the first digits
    else:
        return ccno
    return strng
print(hideccno(ccno))