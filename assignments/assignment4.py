                    #Assignent #4

#Create various data types and experiment its attribute
#1) Name = “some name”
#Convert above string into, upper, lower and capitalize
#Replace ‘e’ with ‘E’ using attribute
#2) L = [1,2,3]
#Extend above list by using [5,6,7] and remove 5th value
#3) d = {‘mango’: 10, ‘banana’: 0, ‘apple’: 15, ‘orange’: 0, ‘pineapple’: 20}
#Remove out of stock fruits from above dictionary
#Update mango quantity into 15 & decrease pineapple b 5

#1

Name = "some name"
Name=Name.upper()
print(Name)

Name=Name.lower()
print(Name)

Name=Name.capitalize()
print(Name)

Name=Name.replace('e','E')
print(Name)

#2

L=[1,2,3]
L+=[5,6,7]
print(L)
del L[4]
print()

#3

d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

for i,j in list(d.items()):
    if j==0:
        del d[i]
    print(i,j)

                    #Updating a dictionary
d['mango']=15
d['pineapple']=d['pineapple']-5
print(d)
