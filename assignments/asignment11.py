                              # Assignment  #11     
'''
Create a Generator function to replicate range()
Create a Recursive function to replicate range()
Create a Recursive and lambda function - Greatest Common Divisor (GCD)
Create A module using an Editor / IDE'''
        
              #Range Function Using Generator
b=0
def range(inp):
  global b
  while b < inp:
    yield b
    b += 1
a = range(10)
print("Range Function Using Generator")
for value in a:
    print(value)

                            #Range Function Using Recursion
start=0
l=[]
def range(rec):
    global start
    if start<rec:
        l.append(start)
        start+=1
        range(rec)
    return
a=range(10)
print("Range Function Using Recursion")
print(l)

                            #GCD Using Lamda and recursion

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print("GCD Using Lamda and recursion")
print(f"The GCD of {num1} and {num2} is {result}")

