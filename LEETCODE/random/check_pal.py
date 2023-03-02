def check_pal(x):
    l, r = 0, len(x)-1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True

print(check_pal("hello"))