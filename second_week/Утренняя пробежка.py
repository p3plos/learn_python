'''
В первый день спортсмен пробежал X километров, а затем он каждый день
увеличивал пробег на 10% от предыдущего значения (для решения задачи
разрешается использовать числа с запятой, которые в Питоне пишутся
через точку).

По данному числу X определите номер дня, на который пробег спортсмена
составит не менее Y километров.

Формат ввода
Программа получает на вход числа X и Y.

Формат вывода
Программа должна вывести одно натуральное число.
'''
#Ответ:
X = int(input())
Y = int(input())
i = 1
while X < Y:
    X *= 1.1
    i += 1
print(i)
