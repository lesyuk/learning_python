x = [int(i) for i in input().split()]

m = max(x) # наибольший элемент в списке
i = x.index(m) # первого индекса первого вхождения элемента в список
print(m)
print(i)