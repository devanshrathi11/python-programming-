ls = []

n = int(input("how many number do you want to enter ? : - "))

for i in range(n):
    num = int(input("ENTER THE NUMBER = "))
    ls.append(num)

lgst = max(ls)
print(ls)

print("THE LARGEST NUMBER IS ",lgst)