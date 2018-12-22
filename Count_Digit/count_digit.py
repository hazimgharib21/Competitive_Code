
def nb_dig(n,d):
    count = 0
    for i in range(n + 1):
        num = str(pow(i,2))
        numArr = list(num)
        for char in numArr:
            if str(d) == char:
                count += 1
    print(count)
    return count

testCase = [
    [10, 1],
    [25, 1],
    [5750,0],
    [11011,2],
    [12224,8],
    [11549,1],
]

outCase = [
    4,
    11,
    4700,
    9481,
    7733,
    11905,
]

for i in range(len(testCase)):
    output = nb_dig(testCase[i][0], testCase[i][1])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))