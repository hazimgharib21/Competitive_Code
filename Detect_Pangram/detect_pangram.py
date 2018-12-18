allChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','']

def is_pangram(s):
    result = []
    charArr = list(s.lower())
    for char in charArr:
        for item in allChar:
            if item == char:
                result.append(item)

    result = set(result)

    return len(result) == 26

testCase = [
    "The quick, brown fox jumps over the lazy dog!",
    "Cwm fjord bank glyphs vext quiz",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ",
    "This isn't a pangram!",
    "abcdefghijklmopqrstuvwxyz",
]

outCase = [
    True,
    True,
    True,
    True,
    True,
    False,
    False,

]

for i in range(len(testCase)):
    output = is_pangram(testCase[i])
    if output == outCase[i]:
        print("Test Case {} Passed".format(i + 1))
    else:
        print("Result {0} - {1} expected".format(output, outCase[i]))