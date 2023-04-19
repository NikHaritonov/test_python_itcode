number=int(input("Введите число "))
flag=True
for i in range(2, number+1):
    if (number%i==0 and i!=number):
        print("Составное")
        flag=False
        break
if (number==1):
    flag=False
    print("Составное")
if (flag):
    print("Простое")