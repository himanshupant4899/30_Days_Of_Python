import random


def deal_to_players(deck, number_of_players):
    first_cards = [next(deck) for _ in range(number_of_players)]
    second_cards = [next(deck) for _ in range(number_of_players)]
    hands = zip(first_cards, second_cards)
    print()

    for i, (first_cards, second_cards) in enumerate(hands, start=1):
        print(f"Player {i} was dealt: {first_cards},{second_cards}")

    print()


def deal_to_table(deck):
    next(deck)
    flop = ','.join(str(next(deck)) for _ in range(3))
    print(f"Flop: {flop}")

    next(deck)
    print(f"The turn: {next(deck)}")

    next(deck)
    print(f"The turn: {next(deck)}")
    print()

def deal(cards, number_of_players):
    deck = shuffle_cards(cards)
    deal_to_players(deck, number_of_players)
    deal_to_table(deck)


def shuffle_cards(card_set):
    deck = card_set
    random.shuffle(deck)
    return iter(deck)


def get_players():
    while True:
        number_of_players = input("Enter the number of players: ").strip()
        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("Value entered should be an integer")
        else:
            if number_of_players in range(2, 11):
                return number_of_players
            elif number_of_players < 2:
                print("There should be at least 2 players.")
            else:
                print("The maximum number of players can be 10.")


ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen", "ace"]
suits = ["hearts", "diamonds", "spades", "clubs"]

cards = [(rank, suit) for rank in ranks for suit in suits]
deal(cards, get_players())
