s = "I am learning information security"
res = " "
mkey=15
akey=20
for i in s:
    if i == " ":
        res += i
    elif i.isupper():
        res += chr(((ord(i)-65)*mkey+akey) % 26 + 65)
    else:
        res += chr(((ord(i)-97)*mkey+akey) % 26 + 97)
print("the cipher is :" + res)
sec=""
for i in res:
    if i == " ":
        sec += i
        continue
    elif i.isupper():
        #just remember the pow function format
        sec+=chr((((ord(i)-65)-akey)* pow(mkey,-1,26)) % 26 + 65)
    else:
        sec+=chr((((ord(i)-97)-akey)* pow(mkey,-1,26)) % 26 + 97)
print("the decipher is :" + sec)