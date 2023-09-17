                                #Assignment #5

'''
Write Examples code for concatenation
Write one Examples for each formatting techniques
Go Through Reference site and apply various options into formatting techniques
Write example for each arithmetic operators
Write Example for assignment operators (except: = & +=).
'''
                        #Concatination

name='Hello'
student='Credo_Systemz'
Name_of_student= name+" "+ student
print("Concatination of strings")
print(Name_of_student)
                        # Formatting
name='shan'
x=f"Hi there my name is {name}.Nice to meet you"
print("Formatting of a string")
print(x)

name='shan'
loc='Andhra Pradesh'
print("Hi i am {} and i am from {}".format(name,loc))

a = "My name is {0}, I'm {1}".format("shan",20)
print(a)

a = "My name is {1}, I'm {0}".format(20,"shan")
print(a)

text = "My name is {name}, I'm {age}".format(name = "Shan", age = 20)
print("Formatting of a string")
print(text)

            #Arthimatic Operators --> +,-,*,/,%,**

a=3
b=2
print("Arthimetic '+' operator ")
print(a+b)
print("Arthimetic '-' operator ")
print(a-b)
print("Arthimetic '*' operator ")
print(a*b)
print("Arthimetic '/' operator ")
print(a/b)
print("Arthimetic '%' operator ")
print(a%b)
print("Arthimetic '**' operator ")
print(a**b)

    #Assignment Operators --> =,+=,-=,*=,,**=,/=,//=,%=,&=,|=,^=,>>=,<<=
a,b=6,4
a-=b
print("Assignment Operator for '-'")
print(a)
a,b=6,4
a*=b
print("Assignment Operator for '*'")
print(a)
a,b=6,4
print("Assignment Operator for '**'")
a**=b
print(a)
a,b=6,4
a/=b
print("Assignment Operator for '/'")
print(a)
a,b=6,4
a//=b
print("Assignment Operator for '//'")
print(a)
a,b=6,4
a%=b
print("Assignment Operator for '%'")
print(a)
a,b=6,4
a&=b
print("Assignment Operator for '&'")
print(a)
a,b=6,4
a|=b
print("Assignment Operator for '|'")
print(a)
a,b=6,4
a^=b
print("Assignment Operator for '^'")
print(a)
a,b=6,4
a>>=b
print("Assignment Operator for '>>'")
print(a)
a,b=6,4
print("Assignment Operator for '<<'")
a<<=b
print(a)

