def addBinary(a, b):
    int_a = int(a, 2)
    int_b = int(b, 2)

    sum = int_a + int_b
    result = bin (sum)[2:]
    return result

a = "11"
b = "1"
print(addBinary(a, b))