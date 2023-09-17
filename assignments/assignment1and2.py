                                  #Assigment #1

import random
a = random.randint(1000,10000)
list1=list(str(a))
b=int(input("Enter your number: "))
list2=list(str(b))
cows=0
bulls=0
guess=0
j=0
i=1
try:
    while cows!=4:
            if j>3 and cows!=4:
                print("Earnings Cows:",cows,"Bulls:",bulls)
                cows=0
                bulls=0
                i+=1
                j=0
                b=int(input("Guess your 4 digit number: "))
                b=str(b)
                list2=list(b)
            elif list1[j] == list2[j]:
                cows+=1
                j+=1
            elif list2[j] in list1:
                bulls+=1
                j+=1
            elif list2[j] not in list1 and list2 not in list1:
                j+=1
                continue
 
    print("congratulations!!.. You Guessed Corret!")
    print("Your Total Earnings Cows:",cows,"Bulls:",bulls)
    print("Your No.of guesses are: ",i)
except IndexError:
    print("Your number is not an 4 digit number!!")
    







        




