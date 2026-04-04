def pelindrome(s):
    result=""
    a=len(s)-1
    while a>=0:
        result+=s[a]
        a=a-1
    if result==s:
        print(result)
        print("pelindrome")
    else:
        print(result)
        print("not a pelindrome")
test=int(input("inter number how many time you want to test :"))
for i in range(test):
    s=input("enter a sting for testing :")
    print(pelindrome(s))