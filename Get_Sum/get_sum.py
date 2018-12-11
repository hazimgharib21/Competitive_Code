

def get_sum(a,b):
    if a > b:
        temp = a
        a = b
        b = temp
    
    c = b - a
    d = 0

    for i in range(c + 1):
        d = d + (a + i)
        
    return d
    

testCase = [
    [1, 0],
    [1, 2],
    [0, 1],
    [1, 1],
    [-1, 0],
    [-1, 2],
]

outCase = [
    1,
    3,
    1,
    1,
    -1,
    2,
]

for i in range(len(testCase)):
    output = get_sum(testCase[i][0], testCase[i][1])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))