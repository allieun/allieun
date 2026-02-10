# SWEA 1219 (길찾기)

'''
내가 선택한 방법 : 데이터 저장 가이드처럼 표를 두 개 설정
1. 길이 m의 리스트를 받은 뒤 2단위 씩 끊어서 각각의 리스트 2개에 나눠서 저장 (두 리스트 길이 역시 100)
2. 0부터 99까지의 경로 중 해당 위치 방문 여부를 확인하는 visited 리스트 생성(길이는 역시 100)
3. 만약 두 리스트에 각각의 인덱스에 해당 위치가 채워져 있다면 visited 리스트의 해당 인덱스 위치는 1
4. 현재 위치를 확인할 수 있는 리스트 stack을 만듬
5. stack에서 도시 번호를 pop 했을 때(now), 그 수가 99일 경우는 성공 -> 1 cnffur
5. visited의 now 인덱스가 1일 경우는 이미 방문한 도시(1이 체크되어있지 않는데 번호가 있을 경우는 1로 변경)
6. adj1 먼저 확인한 후 adj2를 확인했을 때 둘 중 하나라도 있다면 그 번호를 stack에 넣어서 해당 과정 반복
7. 과정종료 후 pop을 했을 때 99가 안나온다면 answer = 0으로 마무리
'''

t = 10

for _ in range(1, t+1):
    tc, m = map(int, input().split())
    way = list(map(int, input().split()))
    
    adj_1 = [-1] * 100      # 길이 없음을 전재로 시작하기 위해 -1로 지정
    adj_2 = [-1] * 100
    visited = [0] * 100      # 시작할 때는 아무데도 안 갔으니 false 값인 0으로 지정
    answer = 0

    # 가볼 길이 있으면 그 방향의 값을 담았다가 pop 하는 과정 반복
    for i in range(0, len(way), 2):
        a = way[i]               # i = 현재 인덱스의 숫자 (홀수, 짝수, 그리고 현재 정점)
        b = way[i+1]             # b = 현재 정점에서 연결되어있는 정점 (0 1 0 2 라면 0에서 1과 2로 두 군데 이어져 있음)

        if adj_1[a] == -1:
            adj_1[a] = b
        else:
            adj_2[a] = b
    
    stack = [0]              # 출발점 위치 0
    while stack:
        now = stack.pop()
        if now == 99:
            answer = 1
            break
        if visited[now] == 1:
            continue
        visited[now] = 1

        if adj_1[now] != -1:
            stack.append(adj_1[now])
        if adj_1[now] != -1:
            stack.append(adj_2[now])

    print(f'#{tc} {answer}')








'''
1 16
0 1 0 2 / 1 4 1 3/ 4 8 4 3 / 2 9 2 5 / 5 6 5 7 / 7 99 7 9 / 9 8 9 10 / 6 10 3 7
'''



