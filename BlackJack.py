import random
def deal_card():
    #returns random card from deck
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(card)
    return card


def calculate_score(cards):
    """ Take the list of cards and return the calculated score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif c_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif u_score > 21:
        return "You went over, You Lose ☠️"
    elif c_score > 21:
        return "Opponent went over, You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your Cards: {user_card}, current Score: {user_score}")
        print(f"Computer's Cards: {computer_card[0]}")
        if user_score  == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to end game")
            if user_deal == 'y':
                user_card.append(deal_card())
            elif user_deal == 'n':
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)


    print(f"Your Final hand: {user_card},final score: {user_score}")
    print(f"Computer's Final hand: {computer_card},final score: {computer_score}")
    print(compare(computer_score, user_score))


while input("Do you want to play again? Type 'y' to play again, type 'n' to end game") == 'y':
    print("\n" * 20)
    play_game()



