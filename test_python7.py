number=int(input('Введи число \n'))
num1=number
num2=0
num3=1
lst=[0]
while len(lst)!=num1:
    number=num3
    num3=num2+number
    num2=number
    lst.append(number)
print(lst[num1-1])
