from itertools import combinations



A = {'이름': 'A', '학년': 2, '지인': ['B', 'C'], '성별': 'male'}
B = {'이름': 'B', '학년': 1, '지인': ['C', 'A'], '성별': 'male'}
C = {'이름': 'C', '학년': 3, '지인': ['A', 'B'], '성별': 'female'}

D = {'이름': 'D', '학년': 2, '지인': ['E', 'F'], '성별': 'female'}
E = {'이름': 'E', '학년': 1, '지인': ['F', 'D'], '성별': 'male'}
F = {'이름': 'F', '학년': 4, '지인': ['D', 'E'], '성별': 'male'}

member_list = ['A', 'B', 'C', 'D', 'E', 'F']

all_list = list(combinations(member_list, 3))
for group in all_list:
    for member in group:
        cnt_member_num = 0   # 멤버 0, 1, 2 를 체크한다.
        while True:
            if member in group[cnt_member_num]['지인']:
