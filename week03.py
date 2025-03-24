def my_zip(l1, l2):
    l3 = list()
    length = 0
    if len(l1) < len(l2):
        length = len(l1)
    else:
        length = len(l2)

    for i in range(length):
        l3.append((l1[i], l2[i]))
    return l3

l1 = [45, 5, 22, 31, 7, 19]
l2 = [22, 1, 5, 2, 7, 28, 27, 19, 13, 41]

print(my_zip(l1, l2))
