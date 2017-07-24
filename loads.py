from utils import error


def start_parse(s, index):
    dct = {
        '{': parse_dic,
        '(': parse_tup,
        '[': parse_lst,
        '"': parse_str,
    }
    dct.update(dict.fromkeys(['f', 't', 'n'], parse_bool_none))
    dct.update(dict.fromkeys('1234567890', parse_num))
    func = dct.get(s[index])
    return func(s, index)


def parse_dic(s, index):
    res = {}
    index += 1
    while s[index] != '}':
        key, index = start_parse(s, index)
        index = blank_jump(s, index, ':')
        value, index = start_parse(s, index)
        res[key] = value
        index = blank_jump(s, index, ',', end='}')
    index = blank_jump(s, index, '}')
    return res,index


def parse_lst(s, index):
    lst = []
    index += 1
    while s[index] != ']':
        value, index = start_parse(s, index)
        lst.append(value)
        index = blank_jump(s, index, ',', end=']')
    index = blank_jump(s, index,']')
    return lst, index


def parse_tup(s, index):
    lst = []
    index +=  1
    while s[index] != ')':
        value, index = start_parse(s, index)
        lst.append(value)
        index = blank_jump(s, index, ',')
    index = blank_jump(s, index, ')')
    return tuple(lst),  index



def parse_str(s, index):
    res = ''
    index += 1
    while s[index] != '"':
        res+= s[index]
        index += 1
    index = blank_jump(s, index, '"')
    return res, index


def parse_bool_none(s, index):
    k = s[index]
    dct = {
        't': True,
        'f': False,
        'n': None,
    }
    return dct[k], index + len(str(dct[k]))


def parse_num(s, index):
    res = ''
    while s[index] in '1234567890.':
        res += s[index]
        index += 1
    isfloat = '.' in res
    if isfloat:
        return float(res), index
    else:
        return int(res), index


def blank_jump(s, index, *typ, end=None):
    if s[index] in typ:
        expcs = {
            ',': ', ',
            ':': ': ',
            ']': ']',
            '}': '}',
            ')': ')',
            '"': '"',
        }
        expc = expcs[s[index]]
        digit = len(expc)
        return index + digit
    elif s[index] == end:
        return index
    else:
        raise error(s, index)

def check_end(s, index):
    if index != len(s):
        raise ValueError('Bad Data End!')


def loads(s, index=0):
    result, index = start_parse(s, index)
    check_end(s, index)
    return result


