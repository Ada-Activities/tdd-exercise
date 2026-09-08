VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):

    #invalid input cases
    if len(hand)>5: 
        return "Invalid"

    #assigning scores for every card and calculating total
    score = 0
    for card in hand: 
        if card not in VALID_CARDS: 
            return "Invalid"
        elif card in ["Jack", "Queen", "King"]:
            score += 10
        elif card == "Ace":
            score += 11
        else: 
            score += card

    #finding the number of aces and adjusting score
    ace_count = 0
    ace_count = hand.count("Ace")

    while score > 21 and ace_count: 
        score -= 10

    #final score win/bust
    if score <= 21: 
        return score
    else:
        return "Bust"

    
