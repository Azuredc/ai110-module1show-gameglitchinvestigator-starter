from logic_utils import check_guess

#FIXME: Make sure to store the 1st element of the tuple returned by check_guess ; Add test cases for the game logic

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)[0]
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)[0]
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)[0]
    assert result == "Too Low"


def test_guess_single_digit_low():
    # If secret is 50 and guess is 8, hint should be "Too Low"
    result = check_guess(8, 50)[0]
    assert result == "Too Low"

def test_guess_two_digit_high():
    # If secret is 50 and guess is 80, hint should be "Too High"
    result = check_guess(80, 50)[0]
    assert result == "Too High"