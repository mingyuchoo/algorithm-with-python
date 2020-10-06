def change():
    total = 1260
    count = 0

    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += total // coin  # 환전한 동전 갯수
        total %= coin  # 남은 돈

    print(count)

    return True
