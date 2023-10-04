import random




#  create card list
#  jumble the order of the card list
#  when dealing the new jumbled list, deal the first card of the list


class PlayingCard:

    def __init__(self, given_suit, given_rank, given_value):
        self.__suit = given_suit
        self.__rank = given_rank
        self.__value = given_value

    def __str__(self):
        return f"{self.__suit} {self.__rank} {self.__value}"


class Deck():

    def __init__(self):
        self.pointer = 0
        self.__cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for i in range(4):  # For each suit
            for j in range(13):  # For each rank in suit
                new_card = PlayingCard(suits[i], ranks[j], values[j])
                self.__cards.append(new_card)

        random.shuffle(self.__cards)
        for cards in self.__cards:
            print(cards)

    def shuffle(self):
        # Code to shuffle cards here
        random.shuffle(self.__cards)


    def deal(self):
        # Code to deal a card from the deck
        # take from the shuffled list
        # remove first item of the shuffled list
        card1 = self.__cards[self.pointer]
        card2 = self.__cards[self.pointer + 1]
        self.pointer += 2
        return card1, card2


class Player(Deck):
    def __init__(self, given_name):
        super().__init__()
        self.__name = given_name
        self.__score = 0
        self.__cardhand = []

    def recievecard(self):
        self.__cardhand.append(self.deal())

    def __str__(self):
        output = f"{self.__cardhand}"
        return output






if __name__ == "__main__":
    card = Player("kurt")
    # card.recievecard()
    # print(card.__str__())

    # player_name = input("Enter your name ")
    # game_player = Player(player_name)