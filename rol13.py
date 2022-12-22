import string # string to all alphabet (a-z)

def string_roll_for_13(strings,roll_forward):
    alpha = list(string.ascii_lowercase) # getting a-z in list as alpha 
    number_saver=0      
    new_string_out=''
    wrd_list=[]
    for words in strings:
    	if words.isalpha():
    		if words in alpha:               # checking input words match with list in alpha
    			for v,k in enumerate(alpha): # seperating list key and value
    				if words in k:           # same as 10 line 
    					v += roll_forward
    					if v >= len(alpha)-1: # if key is greater than index of alpha 
    						number_saver = abs(v-(len(alpha)))
    						wrd_list.append(alpha[number_saver])
    					else:
    							wrd_list.append(alpha[v])
    	
    	
    	else:     # if input contains number or symbols are skipped and added here in output
    			wrd_list.append(words)
    return wrd_list # final word list
    
if __name__=='__main__':
    roll = 13 # to rotate by 13 places in alphabet
    print("ROT13 \n ")
    strings = input("Enter string : ") # input string 
    string_out  =  string_roll_for_13(strings.lower(),roll) # calling function 
    new_string = ""
    for i in string_out:
    	new_string +=i
    print("\n {}\n".format(new_string))
