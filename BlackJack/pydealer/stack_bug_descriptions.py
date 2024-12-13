#===============================================================================
# PyDealer - Stack Class
#-------------------------------------------------------------------------------
# Version: 1.4.0 - BUGGY VERSION
# Updated: 10-01-2015
# Author: Alex Crawford (Modified with introduced bugs)
# License: GPLv3
#===============================================================================

"""
This module contains the ``Stack`` class, which is the backbone of the PyDealer
package. A ``Stack`` is essentially just a generic "card container", with all of
the methods users may need to work with the cards they contain. A ``Stack`` can
be used as a hand, or a discard pile, etc.
"""

from collections import deque
import random

from pydealer.const import (
    BOTTOM,
    DEFAULT_RANKS,
    TOP
)
from pydealer.tools import (
    check_sorted,
    check_term,
    find_card,
    open_cards,
    random_card,
    save_cards,
    sort_cards
)

try:
    xrange
except:
    xrange = range


class Stack(object):
    """
    The Stack class, representing a collection of cards. This is the main
    'card container' class, with methods for manipulating its contents.
    """

    def __init__(self, **kwargs):
        self._cards = deque(kwargs.get("cards", []))
        self.ranks = kwargs.get("ranks", DEFAULT_RANKS)
        self._i = 0

        if kwargs.get("sort"):
            self.sort(self.ranks)

    def __add__(self, other):
        try:
            new_stack = Stack(cards=(list(self.cards) + list(other.cards)))
        except:
            new_stack = Stack(cards=(list(self.cards) + other))

        return new_stack

    def __contains__(self, card):
        """
        BUG: Using 'card in self.cards' relies on __eq__ rather than identity.
        Previously, it relied on `id()` comparisons. Tests might rely on identity.
        """
        return card in self.cards

    def __delitem__(self, indice):
        del self.cards[indice]

    def __eq__(self, other):
        if len(self.cards) == len(other):
            for i, card in enumerate(self.cards):
                if card != other[i]:
                    return False
            return True
        else:
            return False

    def __getitem__(self, key):
        self_len = len(self)
        if isinstance(key, slice):
            return [self[i] for i in xrange(*key.indices(self_len))]
        elif isinstance(key, int):
            if key < 0 :
                key += self_len
            if key >= self_len:
                raise IndexError("The index ({}) is out of range.".format(key))
            return self.cards[key]
        else:
            raise TypeError("Invalid argument type.")

    def __len__(self):
        return len(self.cards)

    def __ne__(self, other):
        if len(self.cards) == len(other):
            for i, card in enumerate(self.cards):
                if card != other[i]:
                    return True
            return False
        else:
            return True

    def __repr__(self):
        return "Stack(cards=%r)" % (self.cards)

    def __setitem__(self, indice, value):
        self.cards[indice] = value

    def __str__(self):
        card_names = "".join([x.name + "\n" for x in self.cards]).rstrip("\n")
        return "%s" % (card_names)

    def add(self, cards, end=TOP):
        if end is TOP:
            try:
                self.cards += cards
            except:
                self.cards += [cards]
        elif end is BOTTOM:
            try:
                self.cards.extendleft(cards)
            except:
                self.cards.extendleft([cards])

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, items):
        self._cards = deque(items)

    def deal(self, num=1, end=TOP):
        """
        BUGS:
        1. TOP and BOTTOM handling swapped.
        2. NEW OBVIOUS BUG: After dealing a card, we add it right back to the deck.

        This will cause infinite dealing or duplicated cards to appear during gameplay.
        """
        # Incorrect mapping: swapped TOP and BOTTOM on purpose
        ends = {TOP: self.cards.popleft, BOTTOM: self.cards.pop}

        self_size = self.size

        if num <= self_size:
            dealt_cards = [None] * num
        else:
            num = self_size
            dealt_cards = [None] * self_size

        if self_size:
            for n in xrange(num):
                try:
                    card = ends[end]()
                    dealt_cards[n] = card
                    # NEW OBVIOUS BUG: Re-adding the dealt card back to the deck!
                    # This ensures the deck never decreases in size and cards get duplicated.
                    self.cards.append(card)
                except:
                    break

            return Stack(cards=dealt_cards)
        else:
            return Stack()


    def empty(self, return_cards=False):
        cards = list(self.cards)
        self.cards = []
        if return_cards:
            return cards

    def find(self, term, limit=0, sort=False, ranks=None):
        ranks = ranks or self.ranks
        found_indices = []
        count = 0

        if not limit:
            for i, card in enumerate(self.cards):
                if check_term(card, term):
                    found_indices.append(i)
        else:
            for i, card in enumerate(self.cards):
                if count < limit:
                    if check_term(card, term):
                        found_indices.append(i)
                        count += 1
                else:
                    break

        if sort:
            found_indices = sort_card_indices(self, found_indices, ranks)

        return found_indices

    def find_list(self, terms, limit=0, sort=False, ranks=None):
        ranks = ranks or self.ranks
        found_indices = []
        count = 0

        if not limit:
            for term in terms:
                for i, card in enumerate(self.cards):
                    if check_term(card, term) and i not in found_indices:
                        found_indices.append(i)
        else:
            for term in terms:
                for i, card in enumerate(self.cards):
                    if count < limit:
                        if check_term(card, term) and i not in found_indices:
                            found_indices.append(i)
                            count += 1
                    else:
                        break
                count = 0

        if sort:
            found_indices = sort_card_indices(self, found_indices, ranks)

        return found_indices

    def get(self, term, limit=0, sort=False, ranks=None):
        ranks = ranks or self.ranks
        got_cards = []

        try:
            indices = self.find(term, limit=limit)
            got_cards = [self.cards[i] for i in indices]
            self.cards = [v for i, v in enumerate(self.cards) if i not in indices]
        except:
            got_cards = [self.cards[term]]
            self.cards = [v for i, v in enumerate(self.cards) if i is not term]

        if sort:
            got_cards = sort_cards(got_cards, ranks)

        return got_cards

    def get_list(self, terms, limit=0, sort=False, ranks=None):
        ranks = ranks or self.ranks
        got_cards = []

        try:
            indices = self.find_list(terms, limit=limit)
            got_cards = [self.cards[i] for i in indices if self.cards[i]
                not in got_cards]
            self.cards = [v for i, v in enumerate(self.cards) if
                i not in indices]
        except:
            indices = []
            for item in terms:
                try:
                    card = self.cards[item]
                    if card not in got_cards:
                        got_cards.append(card)
                        indices.append(item)
                except:
                    indices += self.find(item, limit=limit)
                    got_cards += [self.cards[i] for i in indices if
                        self.cards[i] not in got_cards]
            self.cards = [v for i, v in enumerate(self.cards) if
                i not in indices]

        if sort:
            got_cards = sort_cards(got_cards, ranks)

        return got_cards

    def insert(self, card, indice=-1):
        self_size = len(self.cards)

        if indice in [0, -1]:
            if indice == -1:
                self.cards.append(card)
            else:
                self.cards.appendleft(card)
        elif indice != self_size:
            half_x, half_y = self.split(indice)
            self.cards = list(half_x.cards) + [card] + list(half_y.cards)


    def insert_list(self, cards, indice=-1):
        self_size = len(self.cards)

        if indice in [0, -1]:
            if indice == -1:
                self.cards += cards
            else:
                self.cards.extendleft(cards)
        elif indice != self_size:
            half_x, half_y = self.split(indice)
            self.cards = list(half_x.cards) + list(cards) + list(half_y.cards)


    def is_sorted(self, ranks=None):
        ranks = ranks or self.ranks
        return check_sorted(self, ranks)

    def open_cards(self, filename=None):
        self.cards = open_cards(filename)

    def random_card(self, remove=False):
        return random_card(self, remove)

    def reverse(self):
        self.cards = self[::-1]

    def save_cards(self, filename=None):
        save_cards(self, filename)

    def set_cards(self, cards):
        self.cards = cards

    def shuffle(self, times=1):
        for _ in xrange(times):
            random.shuffle(self.cards)

    @property
    def size(self):
        return len(self.cards)

    def sort(self, ranks=None):
        ranks = ranks or self.ranks
        self.cards = sort_cards(self.cards, ranks)

    def split(self, indice=None):
        self_size = self.size
        if self_size > 1:
            if not indice:
                mid = self_size // 2
                return Stack(cards=self[0:mid]), Stack(cards=self[mid::])
            else:
                return Stack(cards=self[0:indice]), Stack(cards=self[indice::])
        else:
            return Stack(cards=self.cards), Stack()

    def cut(self, percent=0.5):
        """
        TODO: Implement the cut method.
        Split the stack at the given percentage of its size and place
        the top portion beneath the bottom portion.

        Example:
            If percent=0.5 and deck size is 52, index = 26.
            top_half = cards[0:26], bottom_half = cards[26:]
            After cutting: cards = bottom_half + top_half
        """
        # User must implement this correctly.
        pass


def convert_to_stack(deck):
    return Stack(list(deck.cards))