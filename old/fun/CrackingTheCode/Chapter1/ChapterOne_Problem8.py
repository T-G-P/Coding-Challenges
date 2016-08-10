def is_substring(str1, str2):
    if str1 in str2:
        return True
    return False


def is_rotation(str1, str2):
    big_str = str1+str1
    if is_substring(str2, big_str):
        return True
    return False

