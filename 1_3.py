def urlify(str, num):
    new_str = ""
    for i in range(0, num):
        if str[i] == " ":
            new_str += "%20"
        else:
            new_str += str[i]
    return new_str
