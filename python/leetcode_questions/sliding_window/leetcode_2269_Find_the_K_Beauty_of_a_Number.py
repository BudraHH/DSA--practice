def divisorSubstrings(num: int, k: int) -> int:
    string = str(num)
    length = len(string)
    l = 0
    r = k - 1
    res = 0
    while r < length:
        n = int(string[l: r + 1])
        if n != 0 and num % n == 0:
            res += 1
        l += 1
        r += 1
    return res





num = 240
k = 2

# num = 430043
# k = 2

print(divisorSubstrings(num,k))