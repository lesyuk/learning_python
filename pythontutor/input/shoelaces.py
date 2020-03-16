a = int(input()) # расстояние между рядами
b = int(input()) # расстояние между дырочками
N = int(input()) # количество дырочек
l = int(input()) # длина свободного конца шнурка

distance = (l * 2) + ((N * 2 - 1) * a) + ((N * 2 - 2) * b)
print(distance)
