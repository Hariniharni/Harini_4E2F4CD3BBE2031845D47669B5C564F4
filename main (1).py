def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
    num=int(input("enter the number to finad factorial:"))
    res=factorial(num)
    print("the factorial of {} is {}".format(num,res))