products=["Молоко", "Йогурт", "Майонез", "Томаты", "Арбуз", "Куркума"]
count=0
for i in products:
    if len(i)%2==0:
        print(i)
        count+=1
