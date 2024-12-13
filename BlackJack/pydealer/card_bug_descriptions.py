#===============================================================================
# PyDealer - Card Class
#-------------------------------------------------------------------------------
# Version: 1.4.0 - BUGGY VERSION
# Updated: 10-01-2015
# Author: Alex Crawford (Modified with introduced bugs)
# License: GPLv3
#===============================================================================

"""
This module contains the ``Card`` class. Each ``Card`` instance represents a
single playing card, of a given value and suit.

"""

from pydealer.const import DEFAULT_RANKS

class Card(object):
    """
    The Card class, each instance representing a single playing card.

    :arg str value:
        The card value.
    :arg str suit:
        The card suit.

    """
    def __init__(self, value, suit):
        """
        Card constructor method.

        :arg str value:
            The card value.
        :arg str suit:
            The card suit.

        """
        self.value = str(value).capitalize()
        self.suit = str(suit).capitalize() if suit else suit
        self.abbrev = card_abbrev(self.value, self.suit)
        self.name = card_name(self.value, self.suit)

    def __eq__(self, other):
        return (
            isinstance(other, Card) and 
            self.value == other.value and 
            self.suit == other.suit
        )

    def __ne__(self, other):
        # BUG: Parentheses changed, causing comparisons with non-Card objects to behave incorrectly.
        # Previously: (isinstance(other, Card) and self.value != other.value) or self.suit != other.suit
        # Now requires the other object to be a Card even if suits differ,
        # potentially causing incorrect equality checks with non-cards.
        return (
            isinstance(other, Card) and (self.value != other.value or self.suit != other.suit)
        )

    def __ge__(self, other):
        # BUG: Changed >= to > in the suit comparison. This subtle alteration means that
        # two cards of the same value and suit won't be considered >= each other.
        if isinstance(other, Card):
            return (
                DEFAULT_RANKS["values"][self.value] >
                DEFAULT_RANKS["values"][other.value] or
                (
                    DEFAULT_RANKS["values"][self.value] >=
                    DEFAULT_RANKS["values"][other.value] and
                    DEFAULT_RANKS["suits"][self.suit] >
                    DEFAULT_RANKS["suits"][other.suit]  # Changed from >= to >
                )
            )
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Card):
            return (
                DEFAULT_RANKS["values"][self.value] >
                DEFAULT_RANKS["values"][other.value] or
                (
                    DEFAULT_RANKS["values"][self.value] >=
                    DEFAULT_RANKS["values"][other.value] and
                    DEFAULT_RANKS["suits"][self.suit] >
                    DEFAULT_RANKS["suits"][other.suit]
                )
            )
        else:
            return False

    def __hash__(self):
        return hash((self.value, self.suit))

    def __repr__(self):
        return "Card(value=%r, suit=%r)" % (self.value, self.suit)

    def __str__(self):
        return "%s" % (self.name)

    def eq(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] ==
                    ranks["values"][other.value] and
                    ranks["suits"][self.suit] ==
                    ranks["suits"][other.suit]
                )
            else:
                return ranks[self.value] == ranks[other.value]
        else:
            return False

    def ge(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] >
                    ranks["values"][other.value] or
                    (
                        ranks["values"][self.value] >=
                        ranks["values"][other.value] and
                        ranks["suits"][self.suit] >=
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.value] >= ranks[other.value]
        else:
            return False

    def gt(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] >
                    ranks["values"][other.value] or
                    (
                        ranks["values"][self.value] >=
                        ranks["values"][other.value] and
                        ranks["suits"][self.suit] >
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.value] > ranks[other.value]
        else:
            return False

    def le(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] <=
                    ranks["values"][other.value] or
                    (
                        ranks["values"][self.value] <=
                        ranks["values"][other.value] and
                        ranks["suits"][self.suit] <=
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.value] <= ranks[other.value]
        else:
            return False

    def lt(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] <
                    ranks["values"][other.value] or
                    (
                        ranks["values"][self.value] <=
                        ranks["values"][other.value] and
                        ranks["suits"][self.suit] <
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.value] < ranks[other.value]
        else:
            return False

    def ne(self, other, ranks=None):
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["values"][self.value] !=
                    ranks["values"][other.value] or
                    ranks["suits"][self.suit] !=
                    ranks["suits"][other.suit]
                )
            else:
                return ranks[self.value] != ranks[other.value]
        else:
            return False


def card_abbrev(value, suit):
    """
    Constructs an abbreviation for the card, using the given
    value, and suit.

    :arg str value:
        The value to use.
    :arg str suit:
        The suit to use.

    :returns:
        A newly constructed abbreviation.
    """
    # BUG: For value "10", changed to "1%s" instead of "10%s".
    if value == "Joker":
        return "JKR"
    elif value == "10":
        return "1%s" % (suit[0])  # Subtle missing '0'
    else:
        return "%s%s" % (value[0], suit[0])


def card_name(value, suit):
    """
    Constructs a name for the card, using the given value,
    and suit.

    :arg str value:
        The value to use.
    :arg str suit:
        The suit to use.

    :returns:
        A newly constructed name.
    """
    # BUG: Convert suit to lowercase, causing unexpected name formatting.
    if value == "Joker":
        return "Joker"
    else:
        return "%s of %s" % (value, suit.lower())
