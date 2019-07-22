def median(A, B):
    m = len(A)
    n = len(B)
    if m > n:
        return median(B, A)
    k = (m + n +1)//2
    left = 0
    right = m
    while left < right:








    while (len(A) > 1) or (len(B) > 1):
        m = len(A)
        n = len(B)


        if m % 2 == 0:
            meda = (A[m // 2] + A[m // 2 -1])/2
        else:
            meda = A[m // 2]

        if n % 2 == 0:
            medb = (B[n // 2] + B[n // 2 -1])/2
        else:
            medb = B[n // 2]

        if meda < medb:
            A = A[(m // 2):m]
            B = B[0:(n // 2)]
        elif meda > medb:
            A = A[0:(m // 2)]
            B = B[(n // 2):n]
        else:
            medium = meda
            break
        if (len(A) <= 1) and (len(B) <= 1):
            medium = (meda + medb) / 2
            break
    return medium


A = [1,2,3,4,5]
B = [6,7,8]
cc = median(A, B)
print(cc)



