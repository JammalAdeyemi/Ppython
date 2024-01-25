# Divisor Game
# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
# • Choosing any x with 0 < x < n and n % x == 0.
# • Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game. Return true if and only if Alice wins the game, assuming both players play optimally.

### Thought Process and Concepts Utilized
## Problem Understanding:
# -The essence of the problem is a two-player turn-based game where players choose a divisor of the current
# number n and subtract it from n to produce a new number. The player who cannot make a move (when n becomes 1)
# loses.
# -The problem statement implies that there is a strategy involved and hints at an underlying pattern that
# determines the winner. Recognizing that the game's outcome is predetermined by the initial value of n is
# crucial.
# -The task is to identify who wins the game when both players make optimal moves. An optimal move is one 
# that leaves the opponent in the least advantageous position on the next turn.

## Algorithm Choice:
# -Mathematical Strategy and Pattern Recognition: Instead of simulating the game (which could be done using
# dynamic programming or recursion), the problem can be approached by recognizing a pattern that dictates 
# the winner. The pattern is that the player who starts with an even number can always win by playing optimally.
# -Even-Odd Strategy: The insight to use is that if n is even, Alice can always subtract 1, handing Bob an 
# odd number, which guarantees that Alice will always get an even number back on her turn. This is optimal
# play for Alice, ensuring she can always make a move, while eventually, Bob cannot.
# -Simplicity of Solution: The solution is a simple modulo operation to check if the starting number n is 
# even. This choice is based on the realization that the game's complexity can be reduced to a straightforward
# condition related to the parity of the initial number.

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Alice wins if and only if n is even
        return n % 2 == 0

## Explanation
# Alice can win if she starts with an even number because she can always perform a move that leaves an odd 
# number to Bob, from which any move will return an even number to Alice. This pattern continues until Bob 
# is forced to take the number 1, and lose, as he cannot make a legal move.

## Time & Space Complexities
# -Time Complexity: O(1), as the solution involves a single modulo operation, which is a constant-time 
# operation.
# -Space Complexity: O(1), since no additional space is required; the solution only evaluates the parity of
# the number n.  
        
        




