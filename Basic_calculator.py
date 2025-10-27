# basic calculator
#Operation 
operation = ("Operations : +,-,*,/")
Operator = input("Enter a operation :" )
print("The operator you have chosen :" , Operator)

#Number input
a=int(input("Enter a number:"))
b=int(input("Enter another number :"))

#Working
if Operator=="+":
    Result= a+b
elif Operator=="-":
    Result=a-b
elif Operator=="*":
    Result=a*b
elif Operator=="/":
    Result=  a/b
#Result
print("Result=",Result)

