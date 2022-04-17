A = {'이름': 'A', '학년': 2, '지인': ['B', 'C'], '성별': 'male'}
B = {'이름': 'B', '학년': 1, '지인': ['C', 'A'], '성별': 'male'}
C = {'이름': 'C', '학년': 3, '지인': ['A', 'B'], '성별': 'female'}

D = {'이름': 'D', '학년': 2, '지인': ['E', 'F'], '성별': 'female'}
E = {'이름': 'E', '학년': 1, '지인': ['F', 'D'], '성별': 'male'}
F = {'이름': 'F', '학년': 4, '지인': ['D', 'E'], '성별': 'male'}
'''
G = {'이름': 'G', '학년': 3, '지인': ['H', 'J'], '성별': 'female'}
H = {'이름': 'H', '학년': 2, '지인': ['J', 'G'], '성별': 'female'}
J = {'이름': 'J', '학년': 2, '지인': ['G', 'H'], '성별': 'male'}
'''
member_list = ['A', 'B', 'C', 'D', 'E', 'F']

group_1 = [], group_2 = []
com_group_list = [group_1, group_2]        # 가능한 조합 1개
all_group_list = []                                  # 전체 가능한 조합의 리스트

for member in member_list:

    # 조의 인원을 3명으로 맞추는 작업

    cnt = 0  # cnt는 조의 순서이다, 0조 1조 2조...순서
    while True:
        if len(com_group_list) == cnt:
            if len(com_group_list[cnt]) == 3:  # 이미 배정이 끝나서 프로그램이 종료되어야 함(이런 경우가 생길 수가 있나?)
                print('오류코드 1번')
                break

        elif len(com_group_list[cnt]) == 3:  # 넣으려 하는 조의 인원이 이미 3명일 때, 다음 순번의 조로 넘어감
            cnt += 1

    # 지인을 검사해 배제하는 작업, 이때 member 은 com_group_list[cnt] 에 소속될 수 있는지 검사받는다

    if len(com_group_list[cnt]) == 0:  # 이 조에 배정된 인원이 0명일 때
        com_group_list[cnt].append(member)  # member 는 바로 조에 소속된다
    elif len(com_group_list[cnt]) == 1:  # 이 조에 배정된 인원이 1명일 때
        if member in com_group_list[cnt][0]['지인']:  # 이미 배정된 학생의 지인에 member 가 포함된 경우에
            cnt += 1











alist = ['a', 'b', 'c']
