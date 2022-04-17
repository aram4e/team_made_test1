from itertools import combinations

A = {'이름': 'A', '학년': 2, '지인': ['B', 'C'], '성별': 'male'}
B = {'이름': 'B', '학년': 1, '지인': ['C', 'A'], '성별': 'male'}
C = {'이름': 'C', '학년': 3, '지인': ['A', 'B'], '성별': 'female'}

D = {'이름': 'D', '학년': 2, '지인': ['E', 'F'], '성별': 'female'}
E = {'이름': 'E', '학년': 1, '지인': ['F', 'D'], '성별': 'male'}
F = {'이름': 'F', '학년': 4, '지인': ['D', 'E'], '성별': 'male'}


member_list = [A, B, C, D, E, F]

all_list = list(combinations(member_list, 3))
print('all_list 길이', len(all_list))
com_list = list(combinations(all_list, 2))
for group in all_list:
    if group is all_list[0]:
        print('good')
        break
    for member in group:
        for i in range(len(group)):
            if group[i]['이름'] in member['지인']:
                ind = all_list.index(group)
                print(ind)
                del all_list[ind]

print('all_list 길이', len(all_list))