import random
import array
#we will define the max length of the passwd
MAX_LEN = 8
#we will be using the arryas to do this passwd gen
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',  #predeinfed set
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',   #predeinfed set
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
		'*', '(', ')', '<']

# lets get a complete set of the objects we will be using 
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# now using random module we will shuffle all the charcaters to creater a 6 digits
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
#we will just combine to create a 12 or 6 min 6 digit one 
# we want a 6 or 12-character passwdd
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
#here now we have radnom charcters now this, for loops helps in placing all the random ditigs in its places
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	# we have a temp paasswd but we will shuffle to make it bit more harder
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)
#appending the things 
password = ""
for x in temp_pass_list: 
		password = password + x #adding things by increamenting
print(password)# prints the psswd 
