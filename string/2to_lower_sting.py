def to_lower_string(s):
    result=""
    for char in s:
        if 'A'<=char<='Z':
            result+=chr(ord(char)+32)
        else:
            result+=char
    return result
test=int(input("inter number how many time you want to test :"))
for i in range(test):
    s=input("enter a sting for testing :")
    print(to_lower_string(s))