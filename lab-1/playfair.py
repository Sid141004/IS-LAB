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
    char1=''
    if row2==4:
        char2=matrix[0][col2]
    else:
        char2=matrix[row2+1][col2]
    return char1,char2

msg = "The key is hidden under the door pad"
key = "guidance"
msg = remove_spaces(msg)
print(remove_spaces(msg))
print(digraph(msg))
matrix = matrix(key,list1)
print(matrix)
#print(generateKeyTable("hello",list1))