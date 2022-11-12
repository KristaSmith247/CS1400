import random

selection = [
    "Lying On Side",
    "Lying On Side With Dot",
    "Razorback",
    "Trotter",
    "Snouter",
    "Leaning Jowler",
]


def GetRoll():
    """Return a random roll for a pig."""
    pig_roll = random.choice(selection)
    return pig_roll


def is_pig_on_side(pig_roll):
    """Returns true if pig is on its side, otherwise false."""
    return pig_roll == "Lying On Side" or pig_roll == "Lying On Side With Dot"


def get_single_pig_score(pig_roll):
    """Calculate value for single pig roll."""
    roll_score = 0
    if pig_roll == "Razorback":
        roll_score = 5
    elif pig_roll == "Trotter":
        roll_score = 5
    elif pig_roll == "Snouter":
        roll_score = 10
    elif pig_roll == "Leaning Jowler":
        roll_score = 15
    return roll_score


def get_roll_score(pig1_roll, pig2_roll):
    roll_score = 0
    pig1_on_side = is_pig_on_side(pig1_roll)
    pig2_on_side = is_pig_on_side(pig2_roll)
    # If both pigs land on their sides
    if pig1_on_side and pig2_on_side:
        if pig1_roll == pig2_roll:
            roll_score = 1
        else:
            roll_score = 0
    # if only one pig on side
    elif pig1_on_side or pig2_on_side:
        roll_score = get_single_pig_score(pig1_roll) + get_single_pig_score(pig2_roll)
    # if neither pig is on its side
    else:
        if pig1_roll == "Razorback" and pig2_roll == "Razorback":
            roll_score = 20
        elif pig1_roll == "Trotter" and pig2_roll == "Trotter":
            roll_score = 20
        elif pig1_roll == "Snouter" and pig2_roll == "Snouter":
            roll_score = 40
        elif pig1_roll == "Leaning Jowler" and pig2_roll == "Leaning Jowler":
            roll_score = 60
        else:
            roll_score = get_single_pig_score(pig1_roll) + get_single_pig_score(
                pig2_roll
            )
    print("Roll score: ", roll_score, pig1_roll, pig2_roll)
    return roll_score


def pass_the_pig():
    player1_score = 0
    player2_score = 0
    while player1_score < 100 and player2_score < 100:
        pig1_roll = GetRoll()
        pig2_roll = GetRoll()
        player1_score += get_roll_score(pig1_roll, pig2_roll)
        # for when player 1 hasn't gotten 100 points
        if player1_score < 100:
            player2_score += get_roll_score(pig1_roll, pig2_roll)
    winner_string = ""
    print("final scores = ", player1_score, player2_score)
    if player1_score >= 100:
        winner_string = "player 1 wins"
    else:
        winner_string = "player 2 wins"
    return player1_score, player2_score, winner_string


if __name__ == "__main__":
    (player1_score, player2_score, winner_string) = pass_the_pig()
    print(winner_string)
    print(player1_score, player2_score)
