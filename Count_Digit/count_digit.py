
def nb_dig(n,d):
    
    return True

testCase = [
    [5750, 0],
]

outCase = [
    4700,
]

for i in range(len(testCase)):
    output = nb_dig(testCase[i][0], testCase[i][1])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))