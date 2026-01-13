import random


class Card:
    RANKS = ["JOKER","A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITS = ["♥", "♦", "♠", "♣"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # カードの強さの取得
    @property
    def strength(self):
        return Card.RANKS.index(self.rank)

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    # 山札の初期化
    def __init__(self):
        self.cards = []
        for rank in Card.RANKS:
            if rank != "JOKER":
                for suit in Card.SUITS:
                    self.cards.append(Card(rank, suit))
            else:
                self.cards.append(Card(rank,""))

    # 山札のシャッフル
    def shuffle_card(self):
        random.shuffle(self.cards)

    def deal(self, players):
        num_players = len(players)
        player_index = 0
        while len(self.cards) > 0:
            card = self.cards.pop()
            players[player_index].hand.append(card)
            player_index = (player_index + 1) % num_players


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


class GameFlow:
    def __init__(self):
        self.pool = []

    # 勝敗(引き分け)判定
    def who_win(self, field):
        strengths = [card.strength for card in field]
        best = min(strengths)

        if strengths.count(best) > 1:
            for card in field:
                if card.rank == "A" and card.suit == "♠":
                    return field.index(card)
            return "draw"

        else:
            return strengths.index(best)

    # 一回の勝負
    def turn(self, players):
        print("戦争!")
        field = []

        for player in players:
            card = player.hand.pop(0)
            print(f"{player.name}のカードは{card.suit}の{card.rank}です。")
            field.append(card)

        self.pool.extend(field)
        winner_id = self.who_win(field)

        if winner_id == "draw":
            print("引き分けです")
        else:
            random.shuffle(self.pool)
            winner = players[winner_id]
            winner.hand.extend(self.pool)
            print(f"プレイヤー{winner.name}が勝ちました。\
プレイヤー{winner.name}はカードを{len(self.pool)}枚もらいました。")
            self.pool = []

    # 最終結果
    def result(self, players):
        ranking = []

        for player in players:
            count = len(player.hand)
            ranking.append([count, player.name])
            print(f"{player.name}の手札の枚数は{count}枚です。", end="")

        print("")

        ranking.sort(key=lambda x: x[0], reverse=True)
        for rank, (count, name) in enumerate(ranking, 1):
            print(f"{name}は{rank}位です。", end="")


def main():
    # プレイヤーの人数と名前の初期化
    num = int(input("プレイヤーの人数を入力してください (2~5) :"))

    players = []
    for i in range(num):
        name = input(f"プレイヤー{i+1}の名前を入力してください:")
        players.append(Player(name))

    # 山札の初期化
    deck = Deck()
    deck.shuffle_card()

    # プレイヤーの手の初期化
    deck.deal(players)

    # ゲーム開始
    game = GameFlow()
    print("戦争を開始します。")
    print("カードが配られました。")

    # 誰かの手札がなくなるまでターンを続ける
    while all(len(h.hand) > 0 for h in players):
        game.turn(players)

    # 結果の表示
    game.result(players)
    print("\n戦争を終了します。")


if __name__ == "__main__":
    main()
