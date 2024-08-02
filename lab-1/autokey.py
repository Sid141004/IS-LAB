def generate_key(msg , key):
    res=[]
    shifted=[]
    count1 = 0
    count2 = 0
    for i in msg:
        if i.isalpha():
            if count1 < len(key):
                res.append(key[count1])
                count1 += 1
                shifted.append(i)
            elif count2 < len(shifted):
                res.append(shifted[count2])
                count2 += 1
                shifted.append(i)
            else:
                res.append(i)
        else:
            res.append(i)
    return "".join(res)
            
def encrypt(msg , key):
    newkey = generate_key(msg,key)
    res = []
    for i in range(len(msg)):
        if msg[i].isalpha():
            char1 = ord(msg[i])-ord('a')
            char2 = ord(newkey[i])-ord('a')
            res.append(chr((char1+char2)%26+ord('a')))
        else:
            res.append(msg[i])
    return "".join(res)
msg = "the house is being sold tonight"
key = "g"
print(msg)
print(generate_key(msg,key))
print(encrypt(msg,key))