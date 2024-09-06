VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):

    score = 0

    if len(hand) > 5:
        return "Invalid"

    num_aces = 0
    
    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        elif card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card == "Ace":
            num_aces += 1
        else:
            score += card

        if score > 21:
            return "Bust"
    
    # at most 1 ace can be 11, the rest must be 1
    if num_aces > 0:
        temp_score  = score + 11 + (num_aces - 1)
        if temp_score > 21:
            score = score + num_aces
        else:
            score = temp_score

    if score > 21:
        return "Bust"  
    
    return score