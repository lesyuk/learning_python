c = set()

for obj in objects:
    if id(obj) not in c:
        c.add(id(obj))

print(len(c))