import random

field = []
strength = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["♥", "♦", "♠", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = [f"{rank}{suit}" for rank in ranks for suit in suits]
random.shuffle(deck)

player1_hand = [deck.pop() for _ in range(26)]
player2_hand = [deck.pop() for _ in range(26)]
flg = 1


def get_rank(card):
    return card[:-1]


def win(x, y):

    field.append(x)
    field.append(y)

    rank_x = get_rank(x)
    rank_y = get_rank(y)

    idx_x = strength.index(rank_x)
    idx_y = strength.index(rank_y)

    if idx_x < idx_y:
        player1_hand.extend(field)
        num = len(field)
        result = f"プレイヤー1が勝ちました。プレイヤー1はカードを{num}枚もらいました。"
        field.clear()

    elif idx_x > idx_y:
        player2_hand.extend(field)
        num = len(field)
        result = f"プレイヤー2が勝ちました。プレイヤー2はカードを{num}枚もらいました。"
        field.clear()

    else:
        result = "引き分けです。"

    return result


def main():
    print("戦争を開始します。")
    print("カードが配られました。")

    while len(player1_hand) > 0 and len(player2_hand) > 0:
        print("戦争！")
        x = player1_hand.pop()
        y = player2_hand.pop()
        print(f'プレイヤー1のカードは{x[-1]}の{x[:-1]}です')
        print(f'プレイヤー2のカードは{y[-1]}の{y[:-1]}です')
        msg = win(x, y)
        print(msg)

    if len(player1_hand) == 0:
        print("プレイヤー1の手札がなくなりました。")
        print(f"プレイヤー1の手札の枚数は0枚です。プレイヤー2の手札の枚数は{len(player2_hand)}枚です")
        print("プレイヤー1が2位、プレイヤー2が1位です。")
    else:
        print("プレイヤー2の手札がなくなりました。")
        print(f"プレイヤー1の手札の枚数は{len(player1_hand)}枚です。プレイヤー2の手札の枚数は0枚です")
        print("プレイヤー1が1位、プレイヤー2が2位です。")

    print("戦争を終了します。")


main()
