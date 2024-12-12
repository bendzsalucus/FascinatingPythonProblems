# Monty Hall Simulation Implementation Guide

## Introduction

This guide provides instructions for implementing a Python class to simulate the Monty Hall problem. The simulation evaluates two strategies: sticking with the initial choice and switching after the host reveals doors. Developers are tasked with completing the functions in the provided scaffold and running test cases to validate their implementation.

### Background

The Monty Hall problem is a famous probability puzzle. A contestant chooses one of \( N \) doors, behind one of which is a prize. The host then reveals \( G \) goat doors (doors without prizes). The contestant can either stick with their initial choice or switch to another door. This simulation aims to analyze the probabilities of winning under both strategies.

---

## Steps to Complete

### 1. **Set Up the Environment**

Ensure you have Python 3.8+ installed and `numpy` library available. Install `numpy` if necessary:

```bash
pip install numpy
```

### 2. **Understand the Class Structure**

The `MontyHallSimulation` class contains the following methods:

1. `__init__`: Initializes the simulation.
2. `simulate_prizedoor`: Simulates the placement of prizes behind doors.
3. `simulate_guess`: Simulates the contestant's initial guess.
4. `host_opens_doors`: Simulates the host revealing goat doors.
5. `switch_guess`: Simulates switching the guess after doors are revealed.
6. `win_percentage`: Calculates the win percentage for a given strategy.

---

### 3. **Implement Missing Logic**

Each method in the class has a `#TODO` comment indicating where you need to add functionality. For each method, remove any placeholder #TODO comments and use a combination of manual coding and autocomplete suggestions to implement functionality. Use the following guidance:

#### a. `__init__`
- Initialize the simulation parameters: `nsim`, `N`, and `G`.

#### b. `simulate_prizedoor`
- Generate an array of size `nsim` with random integers between `0` and `N-1` to represent prize doors.

#### c. `simulate_guess`
- Generate an array of size `nsim` with random integers between `0` and `N-1` for contestants' guesses.

#### d. `host_opens_doors`
- Ensure the host does not open the door with the prize or the contestant's guess.
- Use `set` operations and `numpy` to select `G` doors randomly.

#### e. `switch_guess`
- Calculate the new guesses by switching to an unopened door that is neither the original guess nor opened by the host.

#### f. `win_percentage`
- Calculate the percentage of guesses that match the prize doors.

---

### 4. **Run Test Cases**

The `test_monty_hall` function will validate your implementation. The expected results for each test case are:

```plaintext
Simulated win percentage (stick): 32.93%
Simulated win percentage (switch): 67.06%
Test passed for nsim=20000, N=3, G=1
Simulated win percentage (stick): 24.85%
Simulated win percentage (switch): 75.15%
Test passed for nsim=20000, N=4, G=2
Simulated win percentage (stick): 20.09%
Simulated win percentage (switch): 79.91%
Test passed for nsim=20000, N=5, G=3
Simulated win percentage (stick): 16.91%
Simulated win percentage (switch): 41.91%
Test passed for nsim=20000, N=6, G=3
Simulated win percentage (stick): 9.72%
Simulated win percentage (switch): 22.25%
Test passed for nsim=20000, N=10, G=5
Simulated win percentage (stick): 14.16%
Simulated win percentage (switch): 42.95%
Test passed for nsim=50000, N=7, G=4
Simulated win percentage (stick): 12.77%
Simulated win percentage (switch): 21.75%
Test passed for nsim=55000, N=8, G=3
Simulated win percentage (stick): 8.64%
Simulated win percentage (switch): 18.19%
Test passed for nsim=20000, N=12, G=6
```

Each result must fall within a 1% tolerance of the expected value.

---

### 5. **Testing Framework**

Use the following test scaffold in your Python script:

```python
if __name__ == "__main__":
    test_cases = [
        (20000, 3, 1, 33.29, 66.71),  # N=3, G=1
        (20000, 4, 2, 24.97, 75.03),  # N=4, G=2
        (20000, 5, 3, 19.98, 80.02),  # N=5, G=3
        (20000, 6, 3, 16.62, 41.71),  # N=6, G=3
        (20000, 10, 5, 10.01, 22.58), # N=10, G=5
        (50000, 7, 4, 14.24, 42.92),  # N=7, G=4
        (55000, 8, 3, 12.51, 21.89),  # N=8, G=3
        (20000, 12, 6, 8.30, 18.33),  # N=12, G=6
    ]

    for nsim, N, G, expected_stick_win_pct, expected_switch_win_pct in test_cases:
        if test_monty_hall(nsim, N, G, expected_stick_win_pct, expected_switch_win_pct):
            print(f"Test passed for nsim={nsim}, N={N}, G={G}")
        else:
            print(f"Test failed for nsim={nsim}, N={N}, G={G}")
```

---

### Notes for Developers

**Validation**: Use the test cases to ensure correctness and compare your results against the expected outputs.

---

By following this guide, you should be able to complete and validate the Monty Hall simulation successfully. Happy coding!

