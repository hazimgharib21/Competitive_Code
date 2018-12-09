
def dig_pow(n, p):
    strN = str(n)
    sum = 0
    count = 0
    for char in strN:
        sum = sum + (int(char) ** (p + count))
        count = count + 1

    k = sum / n

    if k.is_integer():
        print(k)
    else:
        print("-1")

dig_pow(92, 1)