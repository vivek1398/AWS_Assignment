                                # Assignment #12
'''Create a python module with palindrome, fibo and factorial programs
Invoke palindrome, fibo and factorial with various inputs from another module
Create a Class which consist of palindrome, fibo and factorial
'''
import asignment8and10
print(asignment8and10.palindrome('MadaM'))
print(asignment8and10.fact(4))
print(asignment8and10.fibo(5))

# Creating a Class which consist of palindrome, fibo and factorial

class Name:
    @staticmethod
    def palindrome(a):
        x=str(a)
        if x == x[::-1]:
            return "It is a Palindrome"
        else:
            return "It is not a Palindrome"  
    @staticmethod
    def fibo(n):
        out = [0, 1]
        while len(out) < n:
            out.append(out[-1] + out[-2])
        return out
    @staticmethod 
    def fact(a):
        if a==1 or a==0: 
            return 1 
        else: 
            return a*Name.fact(a-1)
  
if __name__=="__main__":
    x=Name()
    print(x.palindrome('dad'))
    print(x.fact(5))
    print(x.fibo(10))
