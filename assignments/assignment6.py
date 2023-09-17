                                        #Assignment #6
'''
Write a program to find power of given number
Explain left/right shift with examples
How & bitwise operator works
How and operator, & operator defers each other.
'''
a=int(input("Enter your base number: "))
b=int(input("enter your power number: "))
c=a**b
print(c)



                                    #Explanation
''' Right Shift Operator: Basically left shift and right shift operators works with
binary digits, 'RIGHT SHIFT' operator shifts the place of binary digits to right side. '''

''' Left Shift Operator: Basically left shift and right shift operators works with
binary digits, 'LEFT SHIFT' operator shifts the place of binary digits to Left side. '''

print("Right and Left Shift Operators")
d=int(input("Enter your first number: ")) #6
e=int(input("enter your second number: ")) #2

f=d<<e  # a = 0000 0110  ---> 0000 1100 = 24
print(f) 

f=d>>e  #0000 0110 ---> 0000 0001 = 1
print(f) 
                                    #Explanation
''' "&" Operator is basically a Bitwise operator it works on bits if any both bits are
same then it considers else it won't. HERE IS THE EXAMPLE FOR BETTER UNDERSTANDING.'''

a=6
b=4
c=a&b   
                                    #Explanation
'''
a=0110  
b=0100 
   |   
 c=0100  --->It comapre both bits from a and b if both are same it considers 
and places in same place of a bit else it won't,so in both a and b the equal
bit is 4 so it represents 0100'''
print("Bitwise '&' operator")
print('a&b =',c)

                    # logical and operator and Bitwise '&' operator
                                #Explanation
''' "and" is a basically logical operator where "&" is a bitwise operator 
"and" operator basically follows ('AND' Gate truth table or logic table) if any 
one is false then it returns false(0) if both are true it returns true(1),
where as "&" operator uses binary bits it checks both bits consists of same bit or not
if it consists same bit then it place the bit in it's same position and rest of all
bits consider as 0'''

                            #Logical and operator
print("Logical and Operator")
a = 10
b = 12
c = 8
if a and b and c:
	print("All the numbers have boolean value as True(1)")
else:
	print("Atleast one number has boolean value as False(0)")
	# 
a = 10
b = 12
c = 0
if a and b and c:
	print("All the numbers consists boolean value as True(1)")
else:
	print("Atleast one number consists boolean value as False(0)")
# 
                        # Bitwise '&' operator
a=6
b=2
c=a&b   
                          #Explanation
'''
a=0110  
b=0010 
   |   
 c=0010  --->It comapre both bits from a and b if both are same it considers 
and places in same place of a bit else it won't,so in both a and b the equal
bit is 2 so it represents 0010'''
print("Bitwise '&' operator")
print('a&b =',c)