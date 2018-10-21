def isBadVersion(n):
    if n >= 2:
        return True
    return False
import math
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    i = 1
    j = n
    mid = (i + j) // 2
    lastTrue = 9999999999999
    while True:
        print(i, j, mid)
        if i == j :
            res = isBadVersion(mid)
            if res and mid < lastTrue:
                lastTrue = mid
            break

        res = isBadVersion(mid)

        if res:
            if mid < lastTrue:
                lastTrue = mid
            j = mid
        else:
            if i == mid:
                i += 1
            else:
                i = mid
        mid = (i + j) // 2
    return lastTrue
print(firstBadVersion(2))