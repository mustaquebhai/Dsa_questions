def non_repeat_string(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    for i in range(len(s)):
        if char_count[s[i]]==1:
            return i
    return -1
test=int(input("inter number how many time you want to test :"))
for i in range(test):
    s=input("enter a sting for testing :")
    print(non_repeat_string(s))