#  find the factorial of number
def Factorial(num):
    factorial=1
    if num==1:
        print(1)
    elif num==-1:
        print("enter valid number")
    else:
        for i in range(1,num+1):
            factorial*=i
        print(factorial)

#test
test_case=int(input("enetr the number how many time you want to test="))
for i in range(test_case):
    num=int(input("enter the number for test="))
    Factorial(num)