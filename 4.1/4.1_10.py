def merge(tup1, tup2):
    l1 = list(tup1)
    l2 = list(tup2)
    merged = []
    while l1 and l2:
        if l1[0] > l2[0]:
            merged.append(l2.pop(0))
        else:
            merged.append(l1.pop(0))
    merged.extend(l1)
    merged.extend(l2)
    return tuple(merged)
