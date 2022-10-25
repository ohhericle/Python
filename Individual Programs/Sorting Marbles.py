""" SORTING MARBLES """

# In a particular board game, there is exactly one row and it comprises N spaces, numbered 0 through N - 1 from left to right. There are also N marbles, numbered 0 through N - 1, initially placed in some arbitrary order. After that, there are two moves available that only can be done one at a time:

# Switch: Switch the marbles in positions 0 and 1.
# Rotate: Move the marble in position 0 to position N - 1, and move all other marbles one space to the left (one index lower).
# The objective is to arrange the marbles in order, with each marble i in position i.

# 1. MarblesBoard Class , represents the game above.

#  __init__ function that takes a starting sequence of marbles (the number of each marble listed in the positions from 0 to N - 1). (Notice in the sequence all the marbles are different numbers and are sequential numbered but not in order!)
# switch() and rotate() methods to simulate the player's moves as described above.
# W is_solved(), that returns True if the marbles are in the correct order or False otherwise.
# Additionally, write __str__ and __repr__ methods to display the current state of the board.

# 2.  Solver Class , that actually plays the MarblesGame.

# __init__ method that takes a MarblesBoard class in its initializer and stores it in an attribute: board.
# solve() method:
# Which repeatedly calls the switch() or the rotate() method of the given MarblesBoard until the game is solved.
# Before the first switch or rotate, make a list of tuples with the starting tuple of ('start', <board starting state>)
# After each step ('switch' or 'rotate'), append to the above list a tuple of:
# What step ('switch' or 'rotate') was performed. Remember, you can only do one switch or one rotate per step!
# The state of the board
# Return the above list as output to this method.
# Solver should strive to make the algorithm reasonably efficient and strive to be the fastest runtime. 

class MarblesBoard:

    def __init__(self, sequence): # Takes a starting sequence of marbles (the number of each marble listed in the positions from 0 to N - 1)
        self.sequence = list(sequence)
    
    def switch (self): # Switch the marbles in positions 0 and 1.
        temp_pos = self.sequence[0]
        self.sequence[0] = self.sequence[1]
        self.sequence[1] = temp_pos

    def rotate (self): # Move the marble in position 0 to position N - 1, and move all other marbles one space to the left (one index lower).
        self.sequence = self.sequence[1:] + self.sequence[:1]

    def is_solved(self): # Returns True if the marbles are in the correct order or False otherwise
        return self.sequence == sorted(self.sequence)

    def __repr__(self): # Display the current state of the board
        return " ".join(map(str, self.sequence)) # Convert list to stirng 

    def __str__(self): # Display the current state of the board
        return " ".join(map(str, self.sequence)) # Convert list to string 

class Solver: 

    def __init__(self, marblesBoard): # Takes a MarblesBoard class in its initializer and stores it in an attribute: board
        self.board = marblesBoard

    def solve(self): # Sort Method
        steps = [("start", str(self.board))]
        n = len(self.board.sequence)
        for i in range (n):
            for j in range (n-1): # Don't compare last item in sequence
                if self.board.sequence[0] > self.board.sequence[1]:
                    # Switch only if element 0 and element 1 are not in order
                    self.board.switch()
                    steps.append(("switch", str(self.board)))
                    if (self.board.is_solved()):
                        return(steps)
                # Always rotate to shift window over
                self.board.rotate()
                steps.append(("rotate", str(self.board)))
                if (self.board.is_solved()):
                    return(steps)
            # Rotate at the end of every pass to shift everything into the right place again
            self.board.rotate()
            steps.append(("rotate", str(self.board)))
            # Return early if board is already solved
            if (self.board.is_solved()):
                return(steps)
        return (steps)