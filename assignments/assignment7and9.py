                                #Assignment #7
'''Refer capitalize function in shared program files, replicate .upper() and .lower() functions
Create a odd sequence from given sequence [1,2,34,65,1,2,65,66,44,33,22,87,123412,09,78,76]
{‘apple’: 10, ‘mango’: 20, ‘pineapple’: 25, ‘orange’: 30, ‘strawberry’: 50, ‘jackfruit’: 10}
Generate a comprehension fruits which has more than 20.
'''
Name = "sathyabama"
Name=Name.upper()
print(Name)

Name=Name.lower()
print(Name)

                                #ODD Sequence

a=[1,2,34,65,1,2,65,66,44,33,22,87,123412,9,78,76]
x=[i for i in a if i%2!=0]
print(x)

                                #comprehension 

d={'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}
updated={i:d[i] for i in d if d[i]>20}
print(updated)