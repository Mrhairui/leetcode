def get_climbing_ways(n):
    if n< 1:
        return 0
    if n == 1:
        return 1
    a = 1
    b = 2
    temp = 0
    for i in range(n):
        temp = a + b
        a = b
        b = temp
    return temp

