'''
Дано трехзначное число. Найдите сумму его цифр.

Формат ввода
Вводится целое положительное число. Гарантируется, что оно соответствует условию задачи.

Формат вывода
Выведите ответ на задачу.
'''
#Ответ:
n = int(input())
print(n // 100 + (n % 100) // 10 + n % 10)
