import json
from loads import loads
'''
todo

unicode
科学计数

'''

string_dic = {'a': 'st', 'b':'td'}
int_dic = {'1': 1, '2': 2,  '3': 3.123}
lst_dic = {'a': [1, 2, 3], 'b': ['1', '2']}
tup_dic = {'a': (1, 2, 3)}
bool_none_dic = {'a': True, 'b': False, 'c': None}
dd = {'name': u'功夫熊猫'}




loads_str = loads(json.dumps(string_dic))
loads_int = loads(json.dumps(int_dic))
loads_lst = loads(json.dumps(lst_dic))
loads_tup = loads(json.dumps(tup_dic))
loads_b_n = loads(json.dumps(bool_none_dic))


assert string_dic == loads_str
assert loads_int == int_dic
assert loads_lst == lst_dic
assert loads_tup == {'a': [1, 2, 3]}
assert loads_b_n == bool_none_dic