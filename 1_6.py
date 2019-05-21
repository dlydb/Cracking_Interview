def str_compress(a_str):
    new_str = list()
    if len(a_str) == 1 or len(a_str) == 0:
        return a_str
    new_str = str_comp(a_str, new_str, 0, 0)
    new_str = ''.join(new_str)
    return new_str if len(new_str) < len(a_str) else a_str

def str_comp(a_str, n_str, pos, num):
    if pos == len(a_str) - 1:
        if a_str[pos] == a_str[pos - 1]:
            n_str.append(a_str[pos] + str(num + 1))
            return n_str
        else:
            n_str.append(a_str[pos])
            return n_str
    elif a_str[pos] == a_str[pos + 1]:
        return str_comp(a_str, n_str, pos + 1, num + 1)
    else:
        n_str.append(a_str[pos] + str(num + 1))
        return str_comp(a_str, n_str, pos + 1, 0)

print (str_compress("abbb"))
