import pydealer

class BlackjackGame:
    """
    Author: Lucus Bendzsa
    A simplified, single-round Blackjack game using pydealer.
    - One player vs. a dealer.
    - Standard rules: player hits or stands, trying not to exceed 21.
      Dealer hits until reaching at least 17.
    - Aces count as 1 or 11, whichever benefits the hand without busting.
    """

    def __init__(self):
        # Create and shuffle the deck
        self.deck = pydealer.Deck()
        self.deck.shuffle()

        self.deck.cut(0.5)
        # Hands are managed as pydealer.Stack or Hand objects
        self.player_hand = self.deck.deal(2)
        self.dealer_hand = self.deck.deal(2)

    def card_value(self, card):
        """
        Returns the blackjack value of a single card.
        Number cards = face value, Face cards = 10, Ace = 11 (adjusted later if needed).
        """
        if card.value.isdigit():
            return int(card.value)
        elif card.value in ["Jack", "Queen", "King"]:
            return 10
        elif card.value == "Ace":
            return 11
        # Just in case, though standard deck shouldn't have others.
        return 0

    def hand_value(self, hand):
        """
        Calculate the best blackjack value of the hand.
        Aces can be 1 or 11, start all Aces as 11, then reduce as needed.
        """
        values = [self.card_value(card) for card in hand]
        total = sum(values)
        # Adjust for Aces if we are busting
        ace_count = sum(1 for card in hand if card.value == "Ace")
        while total > 21 and ace_count > 0:
            # Each ace can be reduced by 10 (from 11 to 1)
            total -= 10
            ace_count -= 1
        return total

    def is_busted(self, hand):
        """Return True if hand value exceeds 21."""
        return self.hand_value(hand) > 21

    def dealer_play(self):
        """
        Dealer draws until hand value >= 17.
        Dealer must follow standard blackjack dealer rules.
        """
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.add(self.deck.deal(1)[0])

    def player_turn(self):
        """
        Player turn logic:
        For this demonstration, we'll prompt the user for actions.
        Player can 'hit' or 'stand'.
        """
        while True:
            val = self.hand_value(self.player_hand)
            print(f"Your hand: {', '.join(str(c) for c in self.player_hand)} (value: {val})")
            if self.is_busted(self.player_hand):
                print("You busted!")
                return
            action = input("Hit or stand? (h/s): ").strip().lower()
            if action == 'h':
                self.player_hand.add(self.deck.deal(1)[0])
            elif action == 's':
                return
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def determine_winner(self):
        """
        Determine the winner after player stands and dealer finishes drawing.
        Compare final hand values.
        """
        player_val = self.hand_value(self.player_hand)
        dealer_val = self.hand_value(self.dealer_hand)
        print(f"\nFinal Hands:")
        print(f"Player: {', '.join(str(c) for c in self.player_hand)} (value: {player_val})")
        print(f"Dealer: {', '.join(str(c) for c in self.dealer_hand)} (value: {dealer_val})")

        if self.is_busted(self.player_hand):
            print("Dealer wins! (Player busted)")
        elif self.is_busted(self.dealer_hand):
            print("Player wins! (Dealer busted)")
        else:
            if player_val > dealer_val:
                print("Player wins!")
            elif dealer_val > player_val:
                print("Dealer wins!")
            else:
                print("It's a tie!")

    def play_round(self):
        """
        Play a single round of Blackjack.
        Steps:
        1. Player turn.
        2. If player not busted, dealer plays.
        3. Determine winner.
        """
        print("Dealer shows:", self.dealer_hand[0])
        self.player_turn()
        if not self.is_busted(self.player_hand):
            self.dealer_play()
        self.determine_winner()


if __name__ == "__main__":
    # Example usage:
    # Run the game and play one round.
    game = BlackjackGame()
    game.play_round()
