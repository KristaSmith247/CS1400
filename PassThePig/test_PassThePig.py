import PassThePig


def test_is_pig_on_side():
    values_to_check = {
        "Lying On Side": True,
        "Lying On Side With Dot": True,
        "Razorback": False,
        "Trotter": False,
        "Snouter": False,
        "Leaning Jowler": False,
        "Not a real type": False,
        None: False,
    }
    for value_to_check in values_to_check.items():
        assert PassThePig.is_pig_on_side(value_to_check[0]) == value_to_check[1]


def test_GetRoll():
    valuesReturned = set()
    for x in range(100):
        valuesReturned.add(PassThePig.GetRoll())
    values_to_check = [
        "Lying On Side",
        "Lying On Side With Dot",
        "Razorback",
        "Trotter",
        "Snouter",
        "Leaning Jowler",
    ]
    for value_to_check in values_to_check:
        assert value_to_check in values_to_check
    assert len(values_to_check) == len(valuesReturned)


def test_get_single_pig_score():
    values_to_check = {
        "Lying On Side": 0,
        "Lying On Side With Dot": 0,
        "Razorback": 5,
        "Trotter": 5,
        "Snouter": 10,
        "Leaning Jowler": 15,
        "Not a real type": 0,
        None: 0,
        "": 0,
    }
    for value_to_check in values_to_check.items():
        assert PassThePig.get_single_pig_score(value_to_check[0]) == value_to_check[1]


def test_get_roll_score():
    values_to_check = [
        # Both pigs land on their sides, same side
        (("Lying On Side", "Lying On Side"), 1),
        (("Lying On Side With Dot", "Lying On Side With Dot"), 1),
        # Both pigs land on their sides, different sides
        (("Lying On Side", "Lying On Side With Dot"), 0),
        (("Lying On Side With Dot", "Lying On Side"), 0),
        # One pig lands on side, other lands on a named side
        (("Lying On Side", "Razorback"), 5),
        (("Razorback", "Lying On Side"), 5),
        (("Lying On Side", "Trotter"), 5),
        (("Trotter", "Lying On Side"), 5),
        (("Lying On Side", "Snouter"), 10),
        (("Snouter", "Lying On Side"), 10),
        (("Lying On Side", "Leaning Jowler"), 15),
        (("Leaning Jowler", "Lying On Side"), 15),
        (("Lying On Side With Dot", "Razorback"), 5),
        (("Razorback", "Lying On Side With Dot"), 5),
        (("Lying On Side With Dot", "Trotter"), 5),
        (("Trotter", "Lying On Side With Dot"), 5),
        (("Lying On Side With Dot", "Snouter"), 10),
        (("Snouter", "Lying On Side With Dot"), 10),
        (("Lying On Side With Dot", "Leaning Jowler"), 15),
        (("Leaning Jowler", "Lying On Side With Dot"), 15),
        # Neither pig is lying on its side
        (("Razorback", "Razorback"), 20),
        (("Trotter", "Trotter"), 20),
        (("Snouter", "Snouter"), 40),
        (("Leaning Jowler", "Leaning Jowler"), 60),
        (("Razorback", "Trotter"), 10),
        (("Razorback", "Snouter"), 15),
        (("Razorback", "Leaning Jowler"), 20),
    ]
    for value_to_check in values_to_check:
        assert (
            PassThePig.get_roll_score(value_to_check[0][0], value_to_check[0][1])
            == value_to_check[1]
        )


def test_pass_the_pig():
    for x in range(1000):
        (player1_score, player2_score, winner_string) = PassThePig.pass_the_pig()
        if player1_score > player2_score:
            assert winner_string == "player 1 wins"
        else:
            assert winner_string == "player 2 wins"
