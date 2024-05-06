def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    stair_a, stair_b = 1, 2

    for _ in range(3, n+1):
        stair_a, stair_b = stair_b, stair_a + stair_b
    return stair_b

print(stairs(3))