'''
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок внутри другой, при
условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

Формат ввода
Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.

Формат вывода
Программа должна вывести одну из следующих строчек:

Boxes are equal, если коробки одинаковые,
The first box is smaller than the second one, если первая коробка может быть
 положена во вторую,

The first box is larger than the second one, если вторая коробка может быть
положена в первую,

Boxes are incomparable, во всех остальных случаях.
'''
#Ответ:
A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())

if A1 > B1:
    A1, B1 = B1, A1
if B1 > C1:
    B1, C1 = C1, B1
if A1 > B1:
    A1, B1 = B1, A1
if A2 > B2:
    A2, B2 = B2, A2
if B2 > C2:
    B2, C2 = C2, B2
if A2 > B2:
    A2, B2 = B2, A2
if A1 == A2 and B1 == B2 and C1 == C2:
    print('Boxes are equal')
elif C1 <= C2 and A1 <= A2 and B1 <= B2:
    print('The first box is smaller than the second one')
elif C1 >= C2 and A1 >= A2 and B1 >= B2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
