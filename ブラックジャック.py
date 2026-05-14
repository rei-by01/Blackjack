# ブラックジャック
import random

# 0 ゲームループ
while True:
    # 勝敗定義
    res = None

    # 0.1 関数を書くスペース
    # --- カード引いたり追加したり ---
    # カードランダムドロー
    def draw_card(x, y):
            x = random.choice(mark_list)
            y = random.choice(card_list)
            return (x, y)


    # カードがダブらないように引く
    def ns_draw_card():
        card = draw_card(0, 1)
        while card in drawncard_list:
            card = draw_card(0, 1)
        return card


    # カードを プレイヤー/引いたカードリスト に追加
    def p_append_card():
        card = ns_draw_card()
        drawncard_list.append(card)
        return card

        
    # ↑のディーラー版
    def d_append_card():
        card = ns_draw_card()
        drawncard_list.append(card)
        return card
    

    # --- ゲーム部分 ---
    # J Q K A の点数変換
    def calc(i):
        if i == "A":
            return 11
        elif i in ["J", "Q", "K"]:
            return 10
        else:
            return i


    # 点数合計
    def card_total(i):
        total = 0
        for c in i:
            total += c
        return total


    mark_list = ["♠", "☘", "♥", "♦"]
    card_list = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    
    # 手札のリスト(点数変換してから追加してる)
    players_card = []
    dealer_card = []
    # 被らないように 1ゲーム内で引いたカードリスト(タプル)
    drawncard_list = []


    # 1 ゲーム開始
    # プレイヤーのカードドロー
    pcard_1 = draw_card(0, 1)
    drawncard_list.append(pcard_1)

    pcard_2 = p_append_card()

    print("あなたのカードは" + str(pcard_1) +
        "と" + str(pcard_2) + "です")

    # ディーラーのカードドロー
    dcard_1 = draw_card(0, 1)
    drawncard_list.append(dcard_1)

    dcard_2 = d_append_card()

    print("ディーラーのカードは" + str(dcard_1) + 
          "ともう一枚はまだ伏せられています")


    # 2 ヒットとスタンド
    # 2.1 点数計算
    players_card.append(calc(pcard_1[1]))
    players_card.append(calc(pcard_2[1]))
    print("現在のあなたの合計値は" , str(card_total(players_card)) , "です")

    # 2.2 ヒットとバースト判定
    while True:
        # バースト判定 続けるループ
        if card_total(players_card) < 21:
            ans = input("yを入力してヒット スタンドの場合はnを押してね: ")
            if ans == "y":
                phit = ns_draw_card()
                drawncard_list.append(phit)
                print(str(phit) + "を引きました")

                k = calc(phit[1])
                players_card.append(k)
                print("現在のあなたの合計値は" + str(card_total(players_card)) + "です")
                continue
            else: print("スタンドしました")
            break

        elif card_total(players_card) > 21:
            res = "lose"
            print("バースト あなたの負け")
            break
        elif card_total(players_card) == 21:
            print("引き分け以上確定！ 自動的にディーラーのターンに移行します")
            break
        

    # 3 ディーラーのターン
    # 3.1 カードオープン + 点数計算
    dealer_card.append(calc(dcard_1[1]))
    dealer_card.append(calc(dcard_2[1]))
    print("ディーラーのカードは", str(dcard_1) + "と" + str(dcard_2) + "で、合計値は" 
        + str(card_total(dealer_card)) + "です")

    # 3.2 プレイヤーがバーストしていたらディーラーはスキップ→結果表示へ
    if res == "lose":
        pass
    else:
        # 3.3 ディーラーの挙動
        while True:
            if card_total(dealer_card) < card_total(players_card):
                dhit = ns_draw_card()
                drawncard_list.append(dhit)
                print("ディーラーは" + str(dhit) + "を引きました")

                k = calc(dhit[1])
                dealer_card.append(k)
                print("現在のディーラーの合計値は" 
                      + str(card_total(dealer_card)) + "です")

                # バースト判定
                if card_total(dealer_card) < 21:
                     continue
                elif card_total(dealer_card) >= 22:
                    print("ディーラーがバーストしました あなたの勝ち")
                    res = "win"
                    break
                elif card_total(dealer_card) == 21:
                    pass

            elif card_total(dealer_card) > card_total(players_card):
                print("あなたの負け")
                break
            elif res == "win":
                pass
            elif card_total(dealer_card) == card_total(players_card):
                print("引き分け！")
                break

    print("最終的な合計値", end=" ")
    print("プレイヤー:" + str(card_total(players_card)) + 
          " ディーラー:" + str(card_total(dealer_card)))
    print("引いたカードテスト" + str(drawncard_list))

    ques = input("もう一度遊びますか？ 遊ぶならyを入力してEnter " \
    "やめるならウインドウを閉じてください:")
    if ques != "y":
        break
