
def OpenOrSenior(data):
    out = []
    for items in data:
        age, handicap = items
        if age >= 55 and handicap > 7:
            out.append("Senior")
        else:
            out.append("Open")

    return out

testCase = [
    [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]],
    [[45, 12],[55, 21],[19, -2],[104, 20]],
    [[3, 12],[55, 1],[91, -2],[54, 23]],
    [[59, 12],[55, -1],[12, -2],[12, 12]],
    [[74, 10],[55, 6],[12, -2],[68, 7]],
    [[16, 23],[56, 2],[56,  8],[54, 6]],
]

outCase = [
    ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior'],
    ['Open', 'Senior', 'Open', 'Senior'],
    ['Open', 'Open', 'Open', 'Open'],
    ['Senior', 'Open', 'Open', 'Open'],
    ['Senior', 'Open', 'Open', 'Open'],
    ['Open', 'Open', 'Senior', 'Open'],
]

for i in range(len(testCase)):
    output = OpenOrSenior(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))