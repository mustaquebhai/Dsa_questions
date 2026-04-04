# Q1. check wheather a number is prime or not
def check_prime(num):
    if num==-1:
        print("not a prime number")
    else:
        for i in range(2,num):
            if num%i==0:
                print("not a prime number")
                break
        else:
            print("it is a primeNumber")
#test 
test_case=int(input("enter the test case howmany time you want to check="))
for i in range(test_case):
    num_test=int(input("enter the number for test="))
    check_prime(num_test)