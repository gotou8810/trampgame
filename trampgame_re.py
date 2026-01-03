import random

class Card:
    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITS = ["♥", "♦", "♠", "♣"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    #カードの強さの取得
    @staticmethod
    def get_strength(card):
        return Card.RANKS.index(card[1:])

class Deck:
    #山札の初期化
    def __init__(self):
        self.cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.cards.append(suit + rank)

    #山札のシャッフル
    def shuffle_card(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Players:
    def __init__(self,num):
        self.num = num
        self.input_names = []

    #入力された名前をリスト化
    def  names(self):
        for i in range(self.num):
            self.input_names.append(str(input(f"プレイヤー{i+1}の名前を入力してください:")))
        return self.input_names
        
    #プレイヤーの手札を二次元リストで管理
    def player_hand(self,cards):
        hands = [[] for _ in range(self.num)]
        
        player_index = 0
        while len(cards) > 0:
            hands[player_index].append(cards.pop())
            player_index = (player_index + 1) % self.num
        
        return hands

class GameFlow:
    def __init__(self):
        self.pool = []

    #勝敗(引き分け)判定
    def who_win(self,field):
        strength = list(map(lambda x : Card.get_strength(x), field))
        best = min(strength)

        if strength.count(best) > 1:
            return "draw"
        
        else:
            return strength.index(best)

    #一回の勝負
    def turn(self,num,hands,names):
        print("戦争!")
        field = []

        for i in range(num):
            card = hands[i].pop(0)
            suit = card[0]
            rank = card[1:]
            print(f"{names[i]}のカードは{suit}の{rank}です。")
            field.append(card)
        
        self.pool.extend(field)
        winner = self.who_win(field)

        if winner == "draw":
            print("引き分けです")

        else:
            hands[winner].extend(self.pool)
            print(f"プレイヤー{winner + 1}が勝ちました。プレイヤー{winner + 1}はカードを{len(self.pool)}枚もらいました。")
            self.pool = []
    
    #最終結果
    def result(self,num,hands,names):
        ranking = []

        for i in range(num):
            count = len(hands[i])
            ranking.append([count,i])
            print(f"{names[i]}の手札の枚数は{count}枚です。", end ="")

        print("")

        ranking.sort(reverse=True)
        for rank, (count, player_index) in enumerate(ranking, 1):
            print(f"{names[player_index]}は{rank}位です。", end="")


def main():
    #プレイヤーの人数と名前の初期化
    num = int(input("プレイヤーの人数を入力してください (2~5) :"))
    players = Players(num)
    names = players.names()

    #山札の初期化
    deck = Deck()
    deck.shuffle_card()

    #プレイヤーの手の初期化
    hands = players.player_hand(deck.cards)

    #ゲーム開始
    game = GameFlow()
    print("戦争を開始します。")
    print("カードが配られました。")

    #誰かの手札がなくなるまでターンを続ける
    while all(len(h) > 0 for h in hands):
        game.turn(num, hands,names)

    #結果の表示
    game.result(num,hands,names)
    print("\n戦争を終了します。")

if __name__ == "__main__":  
    main()
        