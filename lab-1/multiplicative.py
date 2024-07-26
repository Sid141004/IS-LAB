s = "I am learning information security"
res = " "
key=15
for i in s:
    if i == " ":
        res += i
    elif i.isupper():
        res += chr(((ord(i)-65)*key) % 26 + 65)
    else:
        res += chr(((ord(i)-97) * key) % 26 + 97)
print("the cipher is :" + res)
sec=""
for i in res:
    if i == " ":
        sec += i
        continue
    elif i.isupper():
        #just remember the pow function format
        sec+=chr(((ord(i)-65) * pow(15,-1,26)) % 26 + 65)
    else:
        sec+=chr(((ord(i)-97) * pow(15,-1,26)) % 26 + 97)
print("the decipher is :" + sec)