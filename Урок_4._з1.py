﻿print("Определение площади и периметра прямоугольника", "Введите две неравные стороны прямоугольника через пробел (искключение прямоугольник = квадрат)", sep="\n")
a, b = map(int, input().split())
print ("Периметр прямоугольника: " + str(a*2+b*2), "Площадь прямоугольника: " + str(a*b), sep = '\n')