
def find(n):
    sum = 0
    for i in range(1, n + 1):
        if (i % 3) == 0:
            sum += i
            print(i)
        elif (i % 5) == 0:
            sum += i
            print(i)
    return sum

testCase = [
    5,
    10,
    100,
    1000,
]

outCase = [
    8,
    33,
    2418,
    234168,
]

for i in range(len(testCase)):
    output = find(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))