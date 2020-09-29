"""
@Author: ZHANG Mofan
@Time: 09/28/2020 19:00-22:00
       09/29/2020 18:00-23:00

@Author2: XIE Ruiling
"""

import random
from dominoes import dominoes
from multi_sum import two_sum, three_sum


class solitaire:
    def __init__(self):
        self._deck = [(j, i) for i in range(7) for j in range(i+1)]
        self._hand = []

    def shuffle(self):
        """ Knuth-Durstenfeld Shuffle, in place

        Returns
        -------

        """
        temp = []
        for i in range(self.check_nbr_deck()-1, 0, -1):
            p = random.randrange(0, i+1)
            self._deck[i], self._deck[p] = self._deck[p], self._deck[i]

    def check_nbr_deck(self):
        return len(self._deck)

    def check_nbr_hand(self):
        return len(self._hand)

    def draw_domino(self, nbr_max=7):
        """ draw dominoes from the top of the deck (from the end of the deck list)

        Parameters
        ----------
        nbr_max

        Returns
        -------

        """
        nbr_in_deck = self.check_nbr_deck()
        nbr_in_hand = self.check_nbr_hand()
        nbr_to_draw = max(nbr_max - nbr_in_hand, 0)
        print(f"number of dominoes to draw: {nbr_to_draw}.")
        while (nbr_to_draw > 0) and (nbr_in_deck > 0):
            # add one domino to hand
            self._hand.append(self._deck.pop())
            nbr_to_draw -= 1
            nbr_in_deck -= 1

    @staticmethod
    def request_input_string():
        idx_str = input("Please input a string to select the dominoes to pull out: ")
        return idx_str

    def pull_out_domino(self, idx_str):
        """ pull out dominoes from hand

        Parameters
        ----------
        idx_str

        Returns
        -------

        """
        idx_to_delete = [int(i)-1 for i in idx_str]
        if self.check_points(map(self._hand.__getitem__, idx_to_delete)):
            print("Valid input. Dominoes chosen pulled out!")
            self._hand = [self._hand[i] for i in range(self.check_nbr_hand()) \
            if i not in idx_to_delete]
        else:
            print("Invalid input. Please retry!")

    @staticmethod
    def check_points(dominoes):
        # check whether sum of dots is equal to 12
        total_points = 0
        for domino in dominoes:
            total_points += domino[0] + domino[1]
        if total_points == 12:
            return True
        else:
            return False

    def show_domino_in_hand(self):
        # use the function dominoes() to show dominoes in hand
        dominoes(self._hand)

    def check_victory(self):
        # check whether the player won
        if (self.check_nbr_deck() == 0) and (self.check_nbr_hand() == 0):
            return True
        else:
            return False

    def check_defeat(self):
        # 2 sum, 3 sum, 4 sum (3 sum), 5 sum (2 sum), 6 sum (check 1 domino)

        domino_points = [(domino[0] + domino[1]) for domino in self._hand]
        print(domino_points)
        total_points = sum(domino_points)

        # first of all, check if the domino of 12 points is in hand
        # and then check the sum of every 6 dominoes
        for point in domino_points:
            if point == 12:
                return False # the game can continue
            if (total_points - point) == 12:
                return False

        # check the sum of every 2 dominoes
        # and check the sum of every 5 dominoes
        if two_sum(domino_points, 12) or two_sum(domino_points, sum(domino_points)-12):
            return False

        # check the sum of every 3 dominoes
        # and check the sum of every 4 dominoes
        if three_sum(domino_points, 12) or three_sum(domino_points, sum(domino_points)-12):
            return False

        return True # the game can not continue

    def play_game(self):
        # begin a new game
        print("*"*60)
        print("Start a new game.")

        # first, verify that the deck is complete and no domino in hand
        print("Check that the deck is complete and no domino in hand:")
        if (self.check_nbr_deck() != 28) or (self.check_nbr_hand() != 0):
            print("Check failed! Please reinitiate an class object and retry!")
            return

        print("Check passed. Continue the game.")

        # shuffling
        print("Shuffle the deck.")
        self.shuffle()

        # play
        print("Begin playing.")
        turn_nbr = 1
        while (self.check_nbr_deck() > 0) or (self.check_nbr_hand() > 0):
            # check whether the player won
            if self.check_victory():
                print("Victory!")
                break

            # player not won, continue
            print("-"*60)
            print(f"Turn {turn_nbr}")

            # draw dominoes from the top of the deck
            print("Draw dominoes from the deck to hand.")
            self.draw_domino()

            print(f"number of dominoes in deck: {self.check_nbr_deck()}; " \
            + f"number of dominoes in hand: {self.check_nbr_hand()}.")

            # show dominoes in hand
            print("Show all dominoes in hand: ")
            self.show_domino_in_hand()

            # check whether the game can no longer continue
            if self.check_defeat():
                print("Defeat!")
                break

            # request player to select the dominoes to pull out
            idx_str = self.request_input_string()

            # pull out selected dominoes
            self.pull_out_domino(idx_str)

            print("Next turn.\n")
            turn_nbr += 1
        return


"""
#test
t = solitaire()
t.shuffle()
print(t._deck)
t.draw_domino()
print(t._hand)
print(t._deck)
print(len(t._deck))
t.pull_out_domino("123")
print(t._hand)
t.show_domino_in_hand()
t.request_input_string()
"""

test = solitaire()
test.play_game()
