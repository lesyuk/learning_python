def update_dictionary(d, key, value):
    if key not in d:
        key *= 2
        if key not in d:
            d[key] = [value]
        else:
            d[key] += [value]
    else:
        d[key] += [value]