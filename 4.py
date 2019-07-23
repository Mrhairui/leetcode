def median(A, B):
    m = len(A)
    n = len(B)
    if m > n:
        return median(B, A)
    k = (m + n +1)//2  # 不管m+n是偶数还是奇数，这个值都是他们的和的一半
    left = 0
    right = m  # 用两个指针分别指二分法查找的首尾两端
    while left < right:
        m1 = left + (right - left) // 2  # 二分法，也就是查找的通用伎俩，从中间比较，然后一半一半的查找
        m2 = k - m1
        if A[m1] < B[m2 - 1]:  # 由于下标是从零开始的，所以k-2应该是两个下标的和，所以B的right的第一个值是m-1
            left = m1 + 1
        else:
            right = m1

    m1 = left
    m2 = k - m1
    c1 = max(A[m1-1] if m1 > 0 else float('-inf'), B[m2 - 1] if m2 >0 else float('-inf'))  # 一种简单的表达式的方法
    if (m + n) % 2 == 1:
        return c1
    c2 = min(A[m1] if m1 < m else float('inf'), B[m2] if m2 < n else float('inf'))
    return (c1+c2)/2


A = [1,2,3,4,5,6]
B = [5,6,7,8,9,10]
cc = median(A, B)
print(cc)



