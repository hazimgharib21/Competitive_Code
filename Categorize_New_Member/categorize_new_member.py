
def OpenOrSenior(data):
    out = []
    for items in data:
        age, handicap = items
        if age >= 55 and handicap > 7:
            out.append("Senior")
        else:
            out.append("Open")

    print(out)

OpenOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])