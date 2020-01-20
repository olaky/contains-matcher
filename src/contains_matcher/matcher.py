def contains(data, pattern):
    if pattern == []:
        return True
    elif isinstance(data, list):
        for elem in data:
            if (__matches(elem, pattern[0]) and contains(elem, pattern[1:])) or contains(elem, pattern):
                return True
    elif isinstance(data, dict):
        for key in data.keys():
            if __matches(key, pattern[0]):
                if contains(data[key], pattern[1:]):
                    return True
            if contains(data[key], pattern):
                return True
    elif __matches(data, pattern[0]) and len(pattern) == 1:
        return True

    return False

def __matches(element, pattern):
    if element == pattern:
        return True
    return False
