def fa(i, j, a, b, s):
    while i < (len(a) - 1):
        if a[i] <= b[j]:
            s.append(a[i])
            i += 1
        fb(i, j, a, b, s)
    return s


def fb(i, j, a, b, s):
    while j < (len(b) - 1):
        if b[j] <= a[i]:
            s.append(b[j])
            j += 1
        fa(i, j, a, b, s)
    return s


k = list(map(int, input().split()))
l = list(map(int, input().split()))
p = q = 0
c = []

sl = fa(p, q, k, l, c)
print(sl)
