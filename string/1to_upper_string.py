def to_upper_strings(s):
    result=""
    for char in s:
        if 'a'<=char<='z':
            result+=chr(ord(char)-32)
        else:
            result+=char
    return result
test=int(input("inter number how many time you want to test :"))
for i in range(test):
    s=input("enter a sting for testing :")
    print(to_upper_strings(s))