def check(str1, str2):
    if (len(str1) == len(str2)):
        return replace(str1, str2)
    elif (len(str1) == len(str2) - 1):
        return ins_rem(str1, str2)
    elif (len(str2) == len(str1) - 1):
        return ins_rem(str2, str1)
    else:
        return False

def replace(str1, str2):
    dif_found = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if dif_found:
                return False
            dif_found = True
    return True

def ins_rem(str1, str2):
    ind1 = ind2 = 0
    while (ind1 < len(str1) and ind2 < len(str2)):
        if (str1[ind1] != str2[ind2]):
            if (ind1 != ind2):
                return False
            ind2 += 1
        else:
            ind1 += 1
            ind2 += 1
    return True

print(check("pale", "bake"))
