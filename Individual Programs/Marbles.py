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
                    # switch only if element 0 and element 1 are not in order
                    self.board.switch()
                    steps.append(("switch", str(self.board)))
                # always rotate to shift window over
                self.board.rotate()
                steps.append(("rotate", str(self.board)))
            # rotate at the end of every pass to shift everything into the right place again
            self.board.rotate()
            steps.append(("rotate", str(self.board)))
            # return early if board is already solved
            if (self.board.is_solved()):
                return(steps)
        return (steps)




