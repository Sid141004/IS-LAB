def remove_spaces(msg):
    res=[]
    for i in msg:
        if i == " ":
            continue
        else:
            res.append(i)
    return "".join(res)

def msg_matrix(msg,n,m):
    k=0
    for j in range(m):
        for i in range(n):
            a = msg[k]
            matrix[i][j] = ord(a) - 97
            k += 1
def encrypt(msg,key):
    msg = remove_spaces(msg)
    n = int(len(msg)/2)
    m = 2
    msg_matrix(msg,n,m)
    res = [ [0]*2 for x in range(12) ]
    for i in range(12):
        for j in range(2):
            for k in range(2):
                res[i][j] += matrix[i][k]*key[k][j]#2,0,1
                res[i][j] = res[i][j] % 26
    return res
def encrypted(msg,n,m):
    res = []
    for i in range(n):
        for j in range(m):
            res.append(chr(msg[i][j] + 97))
    return "".join(res)
key = [[3,3],[2,7]]
msg = "we live in an insecure worldx"
msg = remove_spaces(msg)
print(msg,"\t",msg[0])
matrix = [[0]*2 for x in range(12) ]
msg_matrix(msg,12,2)
for i in matrix:
    print(i)
print(encrypt(msg,key))
res = encrypt(msg,key)
print(encrypted(res,12,2))
for i in res:
    print(i)
