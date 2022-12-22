import string

def string_roll_for_13(strings,roll_forward):
    alpha = list(string.ascii_lowercase)
    number_saver=0
    new_string_out=''
    wrd_list=[]
    #roll_forward = 1
    for words in strings:
    	if words.isalpha():
    		if words in alpha:
    			for v,k in enumerate(alpha):
    				if words in k:
    					v +=roll_forward
    					if v >= len(alpha)-1:
    						number_saver = abs(v-(len(alpha)))
    						wrd_list.append(alpha[number_saver])
    					else:
    							wrd_list.append(alpha[v])
    	
    	
    	else:
    			wrd_list.append(words)
    return wrd_list
    
if __name__=='__main__':
    roll = 13
    print("ROT13 \n ")
    strings = input("Enter string : ")
    string_out=string_roll_for_13(strings.lower(),roll)
    new_string = ""
    for i in string_out:
    	new_string +=i
    print("\n {}\n".format(new_string))
