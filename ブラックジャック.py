# ブラックジャック
import random

# 0 ゲームループ
while True:
    # 勝敗定義
    res = None

    # 0.1 関数を書くスペース
    # ランダムにカードを一枚引く
    def draw_card():
        return random.choice(card_list)


    '''
    # カードのダブりを確認して、ダブりなら引き直す(未実装)
    def redraw_card(x, y): # 引数どうしよう？
        while True:
            if x == y:
                draw_card
            else:
                break
    '''

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


    card_list = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    # 点数計算用のリスト
    players_card = []
    dealer_card = []


    # 1 ゲーム開始
    pcard_1 = draw_card()
    pcard_2 = draw_card()
    print("あなたのカードは" + str(pcard_1) + "と" + str(pcard_2) + "です")

    dcard_1 = draw_card()
    dcard_2 = draw_card()
    print("ディーラーのカードは" + str(dcard_1) + "ともう一枚はまだ伏せられています")


    # 2 ヒットとスタンド
    # 2.1 点数計算
    players_card.append(calc(pcard_1))
    players_card.append(calc(pcard_2))
    print("現在のあなたの合計値は" , card_total(players_card) , "です")

    # 2.2 ヒットとバースト判定
    while True:
        # バースト判定 続けるループ
        if card_total(players_card) < 21:
            ans = input("yを入力してヒット スタンドの場合はnを押してね: ")
            if ans == "y":
                phit_1 = draw_card()
                print(str(phit_1) + "を引きました")

                k = calc(phit_1)
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
    dealer_card.append(calc(dcard_1))
    dealer_card.append(calc(dcard_2))
    print("ディーラーのカードは", str(dcard_1) + "と" + str(dcard_2) + "で、合計値は" 
        + str(card_total(dealer_card)) + "です")

    # 3.2 プレイヤーがバーストしていたらディーラーはスキップ→結果表示へ
    if res == "lose":
        pass
    else:
        # 3.3 ディーラーの挙動
        while True:
            if card_total(dealer_card) < card_total(players_card):
                dhit_1 = draw_card()
                print("ディーラーは" + str(dhit_1) + "を引きました")

                k = calc(dhit_1)
                dealer_card.append(k)
                print("現在のディーラーの合計値は" + str(card_total(dealer_card)) + "です")

                # バースト判定
                if card_total(dealer_card) < 21:
                     continue
                elif card_total(dealer_card) >= 22:
                    print("ディーラーがバーストしました あなたの勝ち")
                    res = "win"
                    break
                elif card_total(dealer_card) == 21:
                    break

            elif card_total(dealer_card) > card_total(players_card):
                print("あなたの負け")
                break
            elif res == "win":
                pass
            elif card_total(dealer_card) == card_total(players_card):
                print("引き分け！")
                break

    print("最終的な合計値", end=" ")
    print("プレイヤー:" + str(card_total(players_card)) + " ディーラー:" + str(card_total(dealer_card)))

    ques = input("もう一度遊びますか？ 遊ぶならyを入力してEnter やめるならウインドウを閉じてください:")
    if ques != "y":
        break
