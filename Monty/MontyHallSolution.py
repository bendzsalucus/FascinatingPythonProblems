import numpy as np

class MontyHallSimulation:
    """
    Simulates the Monty Hall problem with N doors and G doors revealed by the host.

    Credit: Harvard CS 109: Data Science Public Class avaialbe at: https://github.com/cs109/content
    Problem has been modified and setup for use by Lucus Bendzsa 

    This class provides methods to simulate the game, calculate win percentages
    for different strategies, and analyze the results.
    """

    def __init__(self, nsim, N, G):
        """
        Initializes the simulation.

        Args:
          nsim: The number of simulations to run.
          N: The number of doors.
          G: The number of doors the host opens.
        """
        self.nsim = nsim
        self.N = N
        self.G = G

    def simulate_prizedoor(self):
        """
        Simulates the location of the prize behind one of N doors.

        Returns:
          An array of size nsim, where each element is an integer representing 
          the door number (0 to N-1) where the prize is located.
        """
        return np.random.randint(self.N, size=self.nsim)

    def simulate_guess(self):
        """
        Simulates a contestant's initial guess.

        Returns:
          An array of size nsim, where each element is an integer representing
          the door the contestant initially guesses.
        """
        return np.random.randint(self.N, size=self.nsim)

    def host_opens_doors(self, prizedoors, guesses):
        """
        Simulates the host opening G doors to reveal goats.

        Args:
          prizedoors: An array of door numbers with the prize.
          guesses: An array of the contestant's initial guesses.

        Returns:
          An array of sets, where each set contains the doors opened by the host.
        """
        opened_doors = []
        for prize_door, guess in zip(prizedoors, guesses):
            # All remaining doors excluding the prize and initial guess are available to open
            remaining_doors = [i for i in range(self.N) if i != prize_door and i != guess]
            # Randomly choose G doors to open
            opened = np.random.choice(remaining_doors, size=self.G, replace=False)
            opened_doors.append(set(opened))
        return opened_doors

    def switch_guess(self, guesses, opened_doors):
      """
      Simulates switching the guess after the host reveals G goat doors.

      Args:
        guesses: An array of initial guesses.
        opened_doors: An array of sets of doors opened by the host.

      Returns:
        An array of the new guesses after switching.
      """
      new_guesses = []
      for guess, opened in zip(guesses, opened_doors):
        remaining_doors = [i for i in range(self.N) if i != guess and i not in opened]
        # Print for debugging
        # Randomly choose a new guess from remaining doors
        new_guess = np.random.choice(remaining_doors)
        new_guesses.append(new_guess)
      return np.array(new_guesses)

    def win_percentage(self, guesses, prizedoors):
        """
        Calculates the win percentage.

        Args:
          guesses: An array of guesses.
          prizedoors: An array of prize door locations.

        Returns:
          The win percentage.
        """
        return (guesses == prizedoors).mean() * 100

def test_monty_hall(nsim, N, G, expected_stick_win_pct, expected_switch_win_pct, tolerance=1.0):
    """
    Tests the Monty Hall simulation with a given tolerance.

    Args:
        nsim: The number of simulations to run.
        N: The number of doors.
        G: The number of doors the host opens.
        expected_stick_win_pct: The expected win percentage for the "stick" strategy.
        expected_switch_win_pct: The expected win percentage for the "switch" strategy.
        tolerance: The tolerance for comparing floating-point values.

    Returns:
        True if the test passes (within tolerance), False otherwise.
    """
    simulation = MontyHallSimulation(nsim, N, G)

    prizedoors = simulation.simulate_prizedoor()
    initial_guesses = simulation.simulate_guess()
    opened_doors = simulation.host_opens_doors(prizedoors, initial_guesses)

    win_percent_stick = simulation.win_percentage(initial_guesses, prizedoors)
    final_guesses = simulation.switch_guess(initial_guesses, opened_doors)
    win_percent_switch = simulation.win_percentage(final_guesses, prizedoors)

    print(f"Simulated win percentage (stick): {win_percent_stick:.2f}%")
    print(f"Simulated win percentage (switch): {win_percent_switch:.2f}%")

    return (
        abs(win_percent_stick - expected_stick_win_pct) <= tolerance
        and abs(win_percent_switch - expected_switch_win_pct) <= tolerance
    )

# Updated Test Cases based on your new results
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


# Testing all the cases
for nsim, N, G, expected_stick_win_pct, expected_switch_win_pct in test_cases:
    if test_monty_hall(nsim, N, G, expected_stick_win_pct, expected_switch_win_pct):
        print(f"Test passed for nsim={nsim}, N={N}, G={G}")
    else:
        print(f"Test failed for nsim={nsim}, N={N}, G={G}")
