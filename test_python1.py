day=int(input("Введите день"))
month=input("Введите месяц")
temperature=float(input("Введите температуру"))
print(f"Сегодня {day}.{month} На улице {temperature} градусов")
if temperature < 0:
    print("Холодно, лучше остаться дома")