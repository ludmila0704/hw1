# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

num = int(input("Введите желаемое число рядов елочки: "))
for i in range(0, num):
    print(' ' * (num - i) + '*' * i + '*' * (i + 1))
