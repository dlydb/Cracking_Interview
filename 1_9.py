def str_rot(str, n_str):
    for i in range(1, len(str)):
        str1 = str[:i]
        str2 = str[i:]
        if isSubstring(str1, n_str) and isSubstring(str2, n_str):
            if n_str == str2 + str1:
                return True
    return False
