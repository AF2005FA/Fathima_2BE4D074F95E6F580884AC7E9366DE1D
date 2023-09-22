#1.1 Implement a recursive function to calculate the factorial of a given number
def fact(n):
 if(n==0):
  return 1
 else:
  return n*fact(n-1)
number=int(input("enter a number:"))
res=fact(number)
print("the factorial of{}={}".format(number,res))

