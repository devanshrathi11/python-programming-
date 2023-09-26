n = int (input('ENTER THE NUMBER:'))

a = 0
b = 1
print(a,b, end=' ')
for i in range (2,n):
    next=a+b
    print(next,end=' ')
    a = b
    b = next
   