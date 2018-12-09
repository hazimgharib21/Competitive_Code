

def xo(s):
    totalO = 0
    totalX = 0
    for char in s:
        if char == 'o' or char == 'O':
            totalO = totalO + 1
        elif char == 'x' or char == 'X':
            totalX = totalX + 1
    
    if totalO == totalX:
        print("True")
    else:
        print("False")

xo("xoxo")