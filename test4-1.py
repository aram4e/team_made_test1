from itertools import combinations

A = {'이름': 'A', '학년': 2, '지인': ['B'], '성별': 'm', 'mbti': 'e'}
B = {'이름': 'B', '학년': 1, '지인': ['A'], '성별': 'f', 'mbti': 'i'}

C = {'이름': 'C', '학년': 4, '지인': ['D'], '성별': 'm', 'mbti': 'i'}
D = {'이름': 'D', '학년': 2, '지인': ['C'], '성별': 'f', 'mbti': 'i'}

E = {'이름': 'E', '학년': 3, '지인': ['F'], '성별': 'm', 'mbti': 'e'}
F = {'이름': 'F', '학년': 2, '지인': ['E'], '성별': 'f', 'mbti': 'i'}

member_list = [A, B, C, D, E, F]

all_list = list(combinations(member_list, 3))  # list 안에 튜플로 3명의 인원이 구성된 조 생성, 그 각각의 구성원은 딕셔너리
com_list = list(combinations(all_list, 2))
del_list2 = []

for i in range(len(all_list)):
    for j in range(len(all_list[i])):
        for k in range(len(all_list[i])):
            if all_list[i][j]['이름'] in all_list[i][k]['지인']:
                if i not in del_list2:
                    del_list2.append(i)
for a in reversed(del_list2):
    del all_list[a]
adj_list = all_list  # len(adj_list) == 8

################

com_list2 = list(combinations(adj_list, 2))  # 이후에 매개변수 2 는 전체 조 개수인 9개로 설정된다.

del_list3 = []
for i in range(len(com_list2)):  # 이번에는 28개의 조 구성이 생길 것이다
    g1 = []
    for j in range(len(com_list2[i])):  # 이번에는 2 조씩 묶일 것이다
        for k in range(len(com_list2[i][j])):  # 이번에는 3명이 1조를 구성할 것이다
            g1.append(com_list2[i][j][k]['이름'])
    if len(set(g1)) != 6:
        del_list3.append(i)
for a in reversed(del_list3):
    del com_list2[a]

for i in range(len(com_list2)):
    print(i+1, '번째 구성')
    for j in range(len(com_list2[i])):
        print(j+1, '번째 조')
        for k in range(len(com_list2[i][j])):
            print('이름:' + com_list2[i][j][k]['이름'], '성별:' + com_list2[i][j][k]['성별'], 'mbti:' + com_list2[i][j][k]['mbti'], end=' ')
        print('\n')