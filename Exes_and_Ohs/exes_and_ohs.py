def xo(s):
    totalO = 0
    totalX = 0
    for char in s:
        if char == 'o' or char == 'O':
            totalO = totalO + 1
        elif char == 'x' or char == 'X':
            totalX = totalX + 1
    
    if totalO == totalX:
        return True
    else:
        return False

testCase = [
    "ooxx",
    "xooxx",
    "ooxXm",
    "zpzpzpp",
    "zzoo",
    "xo",
    "XO",
    "xo0",
    "xxxoo",
    "",
    "xxxxxoooxooo",
    "xxxxxoooXooo",
    "abcdefghijklmnopqrstuvwxyz",
]

outCase = [
    True,
    False,
    True,
    True,
    False,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
]

for i in range(len(testCase)):
    output = xo(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))