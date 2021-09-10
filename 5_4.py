src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 66]
dst = [curr for prev, curr in zip(src, src[1:]) if curr > prev]
print(dst)
