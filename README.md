# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

- The game's purpose is to have the user guess the secret number the app generates within a limited amount of attempts.
- Bugs:
   - New game not resetting stats, attempt count, and the game itself
   - Hint's were not provided correctly based on the submitted guesses
   - The secret number not being aligned with the constraint provided by the difficulty selected
- Fixes:
   - Made sure that pressing the new game button cleared the info fro mthe previous game and started a completely new game.
   - Corrected the output message for the hint based on the guess value compared to the secret number.
   - Made sure the secret number was first set to the constrained range set by the difficulty before being generated.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Default difficulty is Normal (which is a range of 1-50)
2. User enters a guess of 35 -> "Too High"
3. User enters a guess of 25 -> "Too Low"
4. Score consistently updates after each guess submission
5. Game ends after the correct guess or all attempts are used up

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py::test_winning_guess PASSED                                                                                [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                               [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                [ 60%]
tests/test_game_logic.py::test_guess_single_digit_low PASSED                                                                       [ 80%]
tests/test_game_logic.py::test_guess_two_digit_high PASSED                                                                         [100%]

=========================================================== 5 passed in 0.08s ===========================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
