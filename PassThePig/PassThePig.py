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


def get_turn_score(player, current_score):
    """Execute a single player's turn."""
    print("\n%s's turn starts with %d\n" % (player, current_score))
    turn_score = 0
    while True:
        pig1_roll = GetRoll()
        pig2_roll = GetRoll()
        roll_score = get_roll_score(pig1_roll, pig2_roll)
        if roll_score == 0:
            turn_score = 0
            break
        turn_score += roll_score
        if turn_score + current_score >= 100:
            break
        print("Your score for this turn is", turn_score)
        if player_wants_to_exit():
            break
    return turn_score


def player_wants_to_exit():
    should_exit = True
    while True:
        player_choice = input("\nDo you want to continue? Y/N ")
        if player_choice == "Y" or player_choice == "y":
            should_exit = False
            break
        if player_choice == "N" or player_choice == "n":
            should_exit = True
            break
        print(
            "That's not a valid option. Only 'Y' or 'N' are valid options. Please try again."
        )
    print()
    return should_exit


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
    print("You got", pig1_roll, "and", pig2_roll, "and it scored", roll_score)
    return roll_score


def pass_the_pig():
    player1_score = 0
    player2_score = 0
    while player1_score < 100 and player2_score < 100:
        player1_score += get_turn_score("Player 1", player1_score)
        # for when player 1 hasn't gotten 100 points
        if player1_score < 100:
            player2_score += get_turn_score("Player 2", player2_score)
    winner_string = ""
    if player1_score >= 100:
        winner_string = "player 1 wins"
    else:
        winner_string = "player 2 wins"
    return player1_score, player2_score, winner_string


if __name__ == "__main__":
    (player1_final_score, player2_final_score, winner_result_string) = pass_the_pig()
    print(winner_result_string)
    print("Final Scores: ", player1_final_score, player2_final_score)
