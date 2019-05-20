def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    check = dict()
    for chr in str1:
        if chr in check.keys():
            check[chr] += 1
        else:
            check[chr] = 1
    for chr in str2:
        if chr not in check.keys():
            return False
        else:
            check[chr] -= 1
            if check[chr] < 0:
                return False
    return True

print(check_permutation("goooopd", "dopooog"))
