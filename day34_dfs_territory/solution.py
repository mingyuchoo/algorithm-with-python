# 공간 크기
n, m = 3, 3

#  공간을 그래프로 모델링
graph = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드를 방문
def dfs(x, y):
    # 주어진 범위를 벗어날 경우에 재귀를 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    # 방문한 노드라면 재귀를 즉시 종료
    else:
        return False


# 영역 개수 저장소
result = 0

# 모든 노드(위치)를 이동하며 DFS 실행하여 방문 처리
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

# 결과 출력
print(result)
