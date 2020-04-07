import sys

print(type(sys.modules)) # <class 'dict'>
print(sys.modules) # key-value for modules

from stepik.course_2.import_system2 import check

print(sys.modules) # updated key-value for modules, can find 'check' module in dict
print(type(check)) # <class 'module'>
print(id(check))

from stepik.course_2.import_system2 import check

print(id(check)) # id doesn't change, reused the same object
