# Blackjack Challenge & Bug Hunt Instructions

Welcome to the **Blackjack Challenge & Bug Hunt**, adapted from the **PyDealer** library. You will run a simplified Blackjack game, identify and fix introduced bugs in the codebase, and enhance the testing suite. These instructions will guide you through the process, point you to helpful AI-assisted coding tools, and provide context for the tasks at hand.

## Overview

**What You Have:**
- A forked version of the **PyDealer** library, which provides classes (`Card`, `Stack`, `Deck`) to manage and manipulate playing cards.
- A simplified **Blackjack game** example, using PyDealer to deal and track cards.
- Intentionally introduced bugs within the `Card`, `Stack`, and/or `Deck` modules that cause test failures and odd game behaviors.

**Your Tasks:**
1. Run the Blackjack game and interact with it to observe any oddities (e.g., infinite cards, duplicated cards, incorrect card ordering).
2. Execute test suites for `test_card`, `test_deck`, and `test_stack` to identify failing tests and understand where the code might be broken.
3. Use AI tools to help locate and fix the bugs. Avoid relying solely on your intuition; the objective is to practice prompting and collaborating with the AI effectively.
4. Implement the `cut()` method in `Stack` and write additional unit tests in `test_Deck` to ensure the new method works as intended.

**Context & Credits:**
- **PyDealer** is a Python library by Alex Crawford designed for easy card and deck manipulation.
- **Blackjack** is a classic card game where players aim to reach a hand value close to 21 without exceeding it.
- The modifications and bugs introduced here are for educational and testing purposes. This scenario helps you learn how to debug, test, and refine code with AI assistance.

## Steps

### 1. Run the Blackjack Game
- Navigate to the directory containing the Blackjack implementation.
- Run the game (e.g., `python blackjack_game.py`) and follow any on-screen instructions.
- Observe unexpected behaviors: infinite dealing, incorrect card names, etc.

### 2. Run the Test Suites
From the Blackjack directory, run the following commands to see verbose test outputs:

```
python -m unittest tests.test_card -v
python -m unittest tests.test_deck -v
python -m unittest tests.test_stack -v
```

Check which tests fail. The verbose output often points directly to methods or lines where the issue may lie.

### 3. Identify & Fix Bugs Using AI Tools
The challenge here is to use the AI tools at your disposal, rather than relying solely on personal debugging experience.

#### Suggested Approach:

**Send Relevant Code Snippets to the AI:**
Copy the code function or method from Stack, Card, or Deck that you suspect is causing issues into your ChatGPT or other AI interface. Ask questions like:
- “I have tests failing that point to this deal() method. Can you spot any logical issues?”
- “I see that the card is re-added to the deck after being dealt. Is that correct?”

**Ask the AI to Explain the Test Failures:**
If a test named `test_deal_from_top` fails, prompt the AI: “Given this test failure, what might be wrong with the `deal()` method?”

**Use Autocomplete/CoPilot:**
Try using your IDE’s AI-assisted autocomplete to see if it suggests a fix when editing the suspect code.

**Iterative Refactoring:**
Once the AI suggests a fix, implement it and re-run the tests. Continue this cycle until tests pass.

Remember: The goal is to rely on the AI’s reasoning. Prompt it with specific questions and provide enough context for it to assist effectively.

### 4. Implement & Test the `cut()` Method
There’s a `cut()` method placeholder in the Stack class. It needs to:
- Split the deck at a given percentage.
- Place the top half beneath the bottom half.

#### Write additional unit tests in `test_Deck` that:
- Check `cut(0.5)` on a standard deck and ensure the order matches expectations.
- Test edge cases like `cut(0)` or `cut(1.0)` (no change scenarios).

#### Use the AI to:
- Help brainstorm test cases.
- Assist in writing the `cut()` method correctly if you get stuck.

### 5. Re-Test & Validate
- After fixing bugs and implementing `cut()`, re-run the tests. All should pass.
- Play the Blackjack game again; it should now run smoothly without infinite cards or incorrect behavior.
- Confirm that all introduced bugs are resolved and the `cut()` functionality works as intended.

## Additional Tips
- **Leverage the AI:** Don’t hesitate to ask the AI to clarify terms, explain code logic, or propose solutions.
- **Incremental Changes:** Make one change at a time, re-run tests to isolate whether that fix worked.
- **Documentation:** If something is unclear, ask the AI to generate docstrings or documentation to better understand the library’s expected behaviors.

## Acknowledgments
- **PyDealer:** GitHub Repository - Original code by Alex Crawford.
- **Adapted Blackjack Challenge:** Modified for educational debugging exercises by Lucus Bendzsa.

Good Luck and Happy Debugging!
