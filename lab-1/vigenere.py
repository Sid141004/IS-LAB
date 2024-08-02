def generate_key(msg , key):
	res = list(key)
	if len(msg) == len(key):
	    return key
	else:
		for i in range(len(msg)-len(key)):
			res.append(key[i%len(key)])
	return "".join(res)
def encrypt(msg , key):
	res = []
	curr_key = generate_key(msg,key)
	for x in range(len(msg)):
	    i = msg[x]
	    if i.isupper():
	        char = chr(((ord(i)+ord(curr_key[x])) - 2*ord('A'))%26 + ord('A'))
	    elif i.islower():
	        char = chr(((ord(i)+ord(curr_key[x])) - 2*ord('a'))%26 + ord('a'))
	    else:
	        char = i
	    res.append(char)
	return "".join(res)
def decrypt(msg,key):
	res= []
	curr_key = generate_key(msg,key)
	for x in range(len(msg)):
	    i = msg[x]
	    if i.isupper():
	        #has to be 26 for some reason in both casess
	        char = chr(((ord(i)-ord(curr_key[x])) + 26)%26 + ord('A'))
	    elif i.islower():
	        char = chr(((ord(i)-ord(curr_key[x])) + 26)%26 + ord('a'))
	    else:
	        char = i
	    res.append(char)
	return "".join(res)
msg = "the House is being sold tonight"
key = "dollars"
encrypted  = encrypt(msg,key)
print(encrypted)
decrypted=decrypt(encrypted,key)
print(decrypted)
