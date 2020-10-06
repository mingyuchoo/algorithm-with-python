def travel(map_size, journey):
    # 초기 위치
    x, y = 1, 1

    # 좌표 이동 수치 설정 (L, R, U, D)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 여정 유형 선언
    move_types = ['L', 'R', 'U', 'D']

    # 여정 확인
    for position in journey:
        next_x = 0
        next_y = 0

        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if position == move_types[i]:
                next_x = x + dx[i]
                next_y = y + dy[i]

        # 공간을 벗어나는 경우 무시 처리
        if next_x < 1 or next_y < 1 or next_x > map_size or next_y > map_size:
            continue

        # 이동 수행
        x, y = next_x, next_y

    return x, y
