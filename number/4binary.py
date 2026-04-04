num=int(input("enter a num: "))
binary=""
while num>0:
    binary=str(num%2)+binary
    num//=2
print(int(binary))
