#check weather a number is pelindrome or not
def Pelindrome(num):
    if num==-1:
        print("enter the valid number")
    else:
        while num>0:
          number=num
          digit=num%10
          num=num/10
          sum=0
          sum=sum*10+digit
        