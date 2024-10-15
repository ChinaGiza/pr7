def ToQuad(Num):
    Res = ""
    if Num < 4:
        Res += str(Num)
    else:
        Res += ToQuad(Num // 4) + str(Num % 4)
    return Res
    
Num = input("Введите целое положительное число: ")
if Num.isdigit():
    print(f"Число {Num} в четверичной системе счисления: {ToQuad(int(Num))}")
else:
    print("Ошибка: значение не является целым положительным числом")