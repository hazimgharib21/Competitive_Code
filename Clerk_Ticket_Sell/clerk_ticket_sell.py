
def tickets(people):
    TwentyFiveBill = 0
    FiftyBill = 0
    HundredBill = 0
    for cash in people:
        if cash == 25:
            TwentyFiveBill += 1
        elif cash == 50:
            TwentyFiveBill -= 1
            FiftyBill += 1
        elif (cash == 100) and (FiftyBill > 0):
            FiftyBill -= 1
            TwentyFiveBill -= 1
            HundredBill += 1
        elif (cash == 100) and (FiftyBill == 0):
            TwentyFiveBill -= 3
            HundredBill += 1
        
        if (TwentyFiveBill < 0) or (FiftyBill < 0) or (HundredBill < 0):
            return False

    return True

testCase = [
    [25, 25, 50],
    [25, 100],
    [25, 25, 50, 50, 100],
    [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [25, 25, 25, 25, 50, 100, 50],
    [50, 100,100],
    [25, 25, 100],
    [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100],
    [25, 25, 50, 50, 100],
    [25, 50, 50],
    [25, 25, 25, 100],
    [25, 50, 25, 100],
    [25, 25, 25, 25, 25, 100, 100],
]

outCase = [
    True,
    False,
    False,
    True,
    False,
    False,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
]

for i in range(len(testCase)):
    output = tickets(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))