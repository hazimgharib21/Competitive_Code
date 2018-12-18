
def tickets(people):
    return False

testCase = [

]

outCase = [

]

for i in range(len(testCase)):
    output = tickets(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))