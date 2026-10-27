import random

# values of cards in blackjack
def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            aces += 1
            total += 11
        else:
            total += int(rank)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

print("\n \n \n<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+> \n \n \n")
player_name = input("Welcome to Blackjack! What is your name? ").strip()
start_game = input(f"\nHello {player_name}, do you want to play a game of Blackjack? (y/n): ").strip().lower()
while start_game == 'y':
    print("\nLet's start!\n")
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print("<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>")
    print(f"\nDealer's hand: [{dealer_hand[0]}, ??]")
    print(f"\n{player_name}'s hand: {player_hand}")
    print(f"{player_name}'s total: {hand_total(player_hand)}")

    hit_or_stand = input("\nDo you want to hit or stand? (h/s): ").strip().lower()
    while hit_or_stand == 'h':
        player_hand.append(deck.pop())
        print(f"\n{player_name}'s hand: {player_hand}")
        print(f"{player_name}'s total: {hand_total(player_hand)}")
        if hand_total(player_hand) > 21:
            print(f"\n{player_name} busts! Dealer wins.")
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Dealer's total: {hand_total(dealer_hand)}")
            break
        hit_or_stand = input("\nDo you want to hit or stand? (h/s): ").strip().lower()

    if hand_total(player_hand) <= 21:
        print(f"\nDealer's hand: {dealer_hand}")
        print(f"Dealer's total: {hand_total(dealer_hand)}")
        while hand_total(dealer_hand) <= 17:
            dealer_hand.append(deck.pop())
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Dealer's total: {hand_total(dealer_hand)}")
        print()
        if hand_total(dealer_hand) > 21:
            print(f"Dealer busts! {player_name} wins.")
        elif hand_total(dealer_hand) > hand_total(player_hand):
            print("Dealer wins.")
        elif hand_total(dealer_hand) < hand_total(player_hand):
            print(f"{player_name} wins.")
        else:
            print("It's a tie. Dealer wins.")  # house always wins in a tie

    start_game = input("\nPlay again? (y/n): ").strip().lower()

print("\nThanks for playing!")
