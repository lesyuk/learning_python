# # идентификатор объекта
# x = [1, 2, 3]
# print(id(x)) # один объект
# print(id([1, 2, 3])) # другой объект
#
# # тип объекта
# type[x]

# def function_name(arg1, arg2):
#     return arg1 + arg2
#
# x = function_name(2, 8)
# y = function_name(x, 21)
# print(y)
# print(type(function_name))
# print(id(function_name(2, 2)))

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(11, 10))