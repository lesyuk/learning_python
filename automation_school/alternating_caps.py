def alternating_caps(s):
    l = list(s)
    letter_counter = 0
    for i in range(len(l)):
        if letter_counter % 2 != 0 and l[i] != ' ':
            l[i] = l[i].lower()
            letter_counter += 1
        elif letter_counter % 2 == 0 and l[i] != ' ':
            l[i] = l[i].upper()
            letter_counter += 1
    return ''.join(l)


print(alternating_caps('OMG this website is awesome!'))