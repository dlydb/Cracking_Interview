def p_p(str):
    dic = dict()
    str = str.lower()
    for chr in str:
        if chr.isalpha():
            if chr in dic.keys():
                dic[chr] += 1
            else:
                dic[chr] = 1
    check = 0
    for key in dic.keys():
        if dic[key] % 2 == 1:
            check += 1
            if check > 1:
                return False
    return True
