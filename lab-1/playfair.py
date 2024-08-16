list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def matrix(key , list1):
    temp1 = []
    for i in key:
        if i not in temp1:
            temp1.append(i)
    matrix = []
    for i in list1:
        if i not in temp1:
            temp1.append(i)
    while temp1 != []:
        matrix.append(temp1[:5])
        temp1 = temp1[5:]
    return matrix
def remove_spaces(msg):
    res=[]
    for i in msg:
        if i == " ":
            continue
        else:
            res.append(i)
    return "".join(res)
def digraph(msg):
    res=[]
    i=0
    while i!= len(msg):
        if i+1 != len(msg):
            if msg[i]!=msg[i+1]:
                res.append(msg[i:i+2])
                i += 2
            else:
                res.append(msg[i]+"x")
                i+=1
        else:
            res.append(msg[i]+"z")
            break
    return res
def encrypt_row(matrix,row1,col1,row2,col2):
    char1=''
    if col1==4:
        char1 = matrix[row1][0]
    else:
        char1 = matrix[row1][col1+1]
    char2=''
    if col2==4:
        char2 = matrix[row2][0]
    else:
        char2 = matrix[row2][col2+1]
    return char1,char2
def encrypt_col(matrix,row1,col1,row2,col2):
    char1=''
    if row1==4:
        char1=matrix[0][col1]
    else:
        char1=matrix[row1+1][col1]
    char2=''
    if row2==4:
        char2=matrix[0][col2]
    else:
        char2=matrix[row2+1][col2]
    return char1,char2
def encrypt_rect(matrix,row1,col1,row2,col2):
    char1=''
    char1=matrix[row1][col2]
    char2=''
    char2=matrix[row2][col1]
    
    return char1,char2
def search(matrix,char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==char:
                return i,j
def encrypt(matrix,msg):
    res=[]
    res1=''
    res2=''
    dia = digraph(msg)
    for i in dia:
        row1,col1 = search(matrix,i[0])
        row2,col2 = search(matrix,i[1])
        
        if row1==row2:
            res1,res2 = encrypt_row(matrix,row1,col1,row2,col2)
        elif col1==col2:
            res1,res2 = encrypt_col(matrix,row1,col1,row2,col2)
        else:
            res1,res2 = encrypt_rect(matrix,row1,col1,row2,col2)
        res1 += res2
        res.append(res1)
    return "".join(res)
        
msg = "the key is hidden under the door pad"
key = "guidance"
msg = remove_spaces(msg)
matrix = matrix(key,list1)
enc = encrypt(matrix,msg)
print("original =", msg)
print("encrypted =" , enc)
print("actual = POCLBXDRLGIYIBCGBGLXPOBILZLTTGIY".lower())

def decrypt_row(matrix,row1,col1,row2,col2):
    char1=''
    if col1==0:
        char1 = matrix[row1][4]
    else:
        char1 = matrix[row1][col1-1]
    char2=''
    if col2==0:
        char2 = matrix[row2][4]
    else:
        char2 = matrix[row2][col2-1]
    return char1,char2

def decrypt_col(matrix,row1,col1,row2,col2):
    char1=''
    if row1==0:
        char1 = matrix[4][col1]
    else:
        char1 = matrix[row1-1][col1]
    char2=''
    if row2==0:
        char2 = matrix[4][col2]
    else:
        char2 = matrix[row2-1][col2]
    return char1,char2
def decrypt_rect(matrix,row1,col1,row2,col2):
    char1=''
    char2=''
    char1 = matrix[row1][col2]
    char2 = matrix[row2][col1]
    return char1,char2
def decrypt(matrix,msg):
    print("\nmatrix is :\n")
    for i in matrix:
        print(i)
    print("\n")
    res=[]
    res1=''
    res2=''
    dia = digraph(msg)
    print("diagraph is:\n\n",dia,'\n')
    for i in dia:
        row1,col1 = search(matrix,i[0])
        row2,col2 = search(matrix,i[1])
        
        if row1==row2:
            res1,res2 = decrypt_row(matrix,row1,col1,row2,col2)
        elif col1==col2:
            res1,res2 = decrypt_col(matrix,row1,col1,row2,col2)
        else:
            res1,res2 = decrypt_rect(matrix,row1,col1,row2,col2)
        if res2 not in 'xz':
            res1 += res2
        res.append(res1)
    return "".join(res)
dec = decrypt(matrix,enc)
print("decrypted = ",dec)
enc = encrypt(matrix,msg)
print(enc)
print("POCLBXDRLGIYIBCGBGLXPOBILZLTTGIY")
print(len(msg),len(enc))
