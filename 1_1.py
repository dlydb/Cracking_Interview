def is_unique(str):
    a_set = set()
    for chr in str:
        if chr in a_set:
            return False
        else:
            a_set.add(chr)
    return True

print (is_unique())
