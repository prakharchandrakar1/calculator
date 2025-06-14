#for addition   

def sum(num1,num2):
    return num1+num2


def substraction(num1,num2):
    return num1-num2


def multiplicaion(num1,num2):
    return num1*num2


def division(num1,num2):
    return num1/num2


def avg(num1,num2):
    return (num1+num2)/2

print("enter the operation :\n "\
    "1.addition \n"\
    "2.substraction\n"\
    "3.multiplication\n"\
    "4.division\n"\
    "5.avg\n")

select = int(input("select operation 1,2,3,4,5:"))

number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))

if select == 1:
    print(number1,"+",number2,"=",\
        sum(number1,number2))
    
elif select == 2:
    print(number1,"-",number2,"=",\
        substraction(number1,number2))
elif select == 3:
    print(number1,"*",number2,"=",\
        multiplicaion(number1,number2))
elif select == 4:
    print(number1,"/",number2,"=",\
        division(number1,number2))
if select == 5:
    print("(number1,"+",number2)", "/" ,"2",
        sum(number1,number2))
else :
    print("the operation is invalid try again!")
