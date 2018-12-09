

def get_sum(a,b):
    if a > b:
        temp = a
        a = b
        b = temp
    
    c = b - a
    d = 0

    for i in range(c + 1):
        d = d + (a + i)
        
    print(d)
    

get_sum(2,2)