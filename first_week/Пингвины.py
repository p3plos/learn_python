'''
Напишите программу, которая по данному числу N от 1 до 9 выводит на экран
N пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между
двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего пингвина. Для упрощения
рисования скопируйте пингвина из примера в среду разработки.
'''
#Ответ:

l1 = '   _~_    '
l2 = '  (o o)   '
l3 = ' /  V  \  '
l4 = '/(  _  )\ '
l5 = '  ^^ ^^   '

N = int(input())
print(l1 * N)
print(l2 * N)
print(l3 * N)
print(l4 * N)
print(l5 * N)
