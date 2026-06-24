# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- The game looks like a typical random number guessing game.
- Bugs
  1. The provided hints are flipped
  2. The "New Game" button doesn't provide a "Secret" number that adheres to the set "Difficulty" setting
  3. When you reach the "Game Over" notification, the "New Game" button doesn't reset the game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                             | Expected Behavior     | Actual Behavior       | Console Output / Error |
|-----------------------------------|-----------------------|-----------------------|------------------------|
| Guess is less than Secret         | Hint says "Go Higher" | Hint says "Go Lower"  |                        |
-------------------------------------------------------------------------------------------------------------|
| Guess is greater than Secret      | Hint says "Go Lower"  | Hint says "Go Higher" |                        |
|------------------------------------------------------------------------------------------------------------|
| Click "New Game button"           | Increment Attempts    | Sets it to 0 each time|                        |
|                                   | counter               |                       |                        |
|------------------------------------------------------------------------------------------------------------|
| Submitting wrong answer multiple  | Score should          | Alternates between -5 |                        |
| times                             | continually decrease  | & 0                   |                        |
-------------------------------------------------------------------------------------------------------------|
| Clicking the "New Game" button    | Give a random number  | Gives a random number |                        |
| gives a random number not         | that is within the    | between 1-100         |                        |
| necessarily in the set range      | range set by the      |                       |                        |
| for the chosen "Difficulty"       | chosen Difficulty     |                       |                        |
|------------------------------------------------------------------------------------------------------------|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Claude Code
- The AI suggested I fix the function for "update_score" which was causing the score to improperly update. It apparently had bad code dealing with even attempts which led to the score alternating between "0" and "-5". Getting rid of the if statement handling even cases corrected the issue in manual testing.
- The AI made a suggesting as to the input type of the value provided to the check guess be hard casted to str. My conception of comparing number values was that it should be int so I thought the opposite of the AI and decided to typecast it to an int. I verified it with print statements checking the types.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


- I made sure to run the app with streamlit and run through the inputs to confirm that the bugs were fixed.
- I set up a test using pytest that ran a single digit guess against a double digit secret which should and did return the correct result of "Too Low". It helped to reaffirm that the logic of the functions were correct.
- I definitely helped me to clearly understand the proper results that I should be outputting. It made clarifications as to the function output being 2 dimensions and I needed to only access the 1st dimension to compare the assertion to.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- The app reloads itself everytime you provide it an input (i.e. clicking). The way the app doesn't forget any of the previous stuff it has on it is through "session state" that saves the necessary things the app needs to show.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


- I'll probably keeping the strategy of prompting the AI in smaller chunks to give it focus and not let it be distracted by too much variables.
- One thing I would want to do different next time is try to have it provide more guided responses rather than just the answer.
- It has really made me realize how helpful to have AI as a tool to help bounce ideas off of and to use as a resource to gain insight from.