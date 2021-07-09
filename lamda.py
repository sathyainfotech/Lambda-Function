"""
    lambda arguments : expression
"""

data=lambda a,b : a+b
result=data(30,20)
print("Lambda:",result)

# def myfun(a,b):
#     c=a+b
#     print("Sum:",c)
# myfun(30,20)

result=lambda num:num%2==0
data=result(16)
print("Result:",data)

if(data==True):
    print("Even Number")
else:
    print("Odd Number")