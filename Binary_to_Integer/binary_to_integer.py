
def binary_array_to_number(arr):
    
    return True

testCase = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
]

outCase = [
    1,
    2,
    5,
    9,
    2,
    6,
    15,
    11,
]

for i in range(len(testCase)):
    output = binary_array_to_number(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))