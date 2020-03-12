from collections import Counter
s = input().split()
for i in range(len(s)):
    s[i] = s[i].lower()
dictionary = Counter(s) # подсчет количества вхождений всех элементов в список и преобразование в словарь
for key, value in dictionary.items():
    print(key, value)
