A = input("Введите положительное число A: ")
B = input("Введите положительное число B (не должен равнятся 0): ")
C = input("Введите положительное число C: ")
if (A.replace(".","",1).isdigit() and 
    B.replace(".","",1).isdigit() and 
    C.replace(".","",1).isdigit()):
    A = float(A)
    B = float(B)
    C = float(C)
    if B:
        X = A / B - 2 * C
        print(f"Решение уравнения X = A / B - 2 * C равен {X}")
    else:
        print("Ошибка: решение уравнения невозможно, так как B равен 0")
else:
    print("Ошибка: значение не является положительным числом")