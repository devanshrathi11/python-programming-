


ls2 = [int(i) for i in input().split()]
ls = []
for i in ls2:
    if i not in ls:
        ls.append(i)
mxm = max(ls)
ls.remove(mxm)
out = max(ls)
print(out)
