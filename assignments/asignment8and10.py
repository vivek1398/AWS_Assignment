                                    # Assignment #8 
'''Create a function to replicate built-in -sum()
Create a function to replicate string attribute like, ljust(), rjust() - Refer Practice files
Create a function to find, Palindrome, Fibo and Factorials
Create a function to generate range of numbers - Refer Practice files
'''
 #sum of  numbers
def sum(i, start=0):
    result = start
    for item in i:
        result += item
    return result
if __name__=="__main__":
  numbers = map(int,input("Enter values:").split(' '))
  total = sum(numbers)
  print(total)

                             #replicating a string attribute like, ljust(), rjust()
def ljust(size, fill = ' '):

  x = input("Enter Your word:")
  if size<=len(x):
    return x
  else:
    right = size-len(x)
    return "{}{}".format(x, fill*right)
if __name__=="__main__":
  print("replicating a string attribute ljust()")
  print(ljust(5,'*'))


def rjust(size, fill = ''):
  x = input("Enter Your word:")
  if size<=len(x):
    return x
  else:
    left = size-len(x)
    return "{}{}".format(fill*left, x)
if __name__=="__main__":
  print("replicating a string attribute like rjust()")
  print(rjust(5,'*'))

                              #Palindrome
def palindrome(a):
    x=str(a)
    if x == x[::-1]:return "It is a Palindrome"
    else:return "It is not a Palindrome"  
if __name__=="__main__":
  print(palindrome('dad'))


                           #Fibonacci series
def fibo(n):
    out = [0, 1]
    while len(out) < n:
        out.append(out[-1] + out[-2])
    return out
if __name__=="__main__":
  print(fibo(10))

                            #Factorial

def fact(a):
    if a==1 or a==0: return 1 
    else: return a*fact(a-1)
if __name__=="__main__":
  print(fact(5))
                            #Range Function
                            

def range(stop):
 out = []
 start = 0
 while start < stop:
   out.append(start)
   start += 1
 return out
if __name__=="__main__":
  print("Creating a Range using Function ")
  print(range(20))