def solution(coin, cards):
    n = len(cards)
    target = n + 1

    hand = set(cards[:n//3])
    deck = cards[n//3:]

    answer = 1

    # 새로 뽑은 카드들 저장
    picked = set()

    for i in range(0, len(deck), 2):
        picked.add(deck[i])
        picked.add(deck[i+1])

        found = False

        # 1️⃣ hand에서 공짜 매칭
        for x in list(hand):
            if target - x in hand:
                hand.remove(x)
                hand.remove(target - x)
                found = True
                break

        # 2️⃣ hand + picked (코인 1, picked에서 1개 고르고, 손에서 1개 고르는 경우)
        if not found and coin >= 1:
            for x in list(hand):
                if target - x in picked:
                    hand.remove(x)
                    picked.remove(target - x)
                    coin -= 1
                    found = True
                    break

        # 3️⃣ picked + picked (코인 2, picked에서 2개 모두 고르는 경우)
        if not found and coin >= 2:
            for x in list(picked):
                if target - x in picked:
                    picked.remove(x)
                    picked.remove(target - x)
                    coin -= 2
                    found = True
                    break

        if not found: # 낼게 없으면 종료
            break

        answer += 1

    return answer