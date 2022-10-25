""" A GAME OF CHESS """

# # You place a pawn at the top left corner of an n-by-n chess board, labeled (0,0). For each move, you have a choice: move the pawn down a single space, or move the pawn down one space and right one space. That is, if the pawn is at position (i,j), you can move the pawn to (i+1,j) or (i+1, j+1).

# Script asks the user for the size of a chessboard, n (integer). Then finds the number of different paths starting from (0,0) that the pawn could take to reach each position on the chess board. For example, there are two different paths the pawn can take to reach (2,1). Look at the diagrams below to convince yourself of this. You can see the four paths that you can take by move 2.

#   Start -> Move 1 -> Move 2

#   (0,0) ->  (1,0) -> (2,1)

#   (0,0) ->  (1,0) -> (2,0)

#   (0,0) ->  (1,1) -> (2,1)

#   (0,0) ->  (1,1) -> (2,2)
# Prints the board with the number of ways to reach each square labeled as shown below.

# Get the user input for the board size
n = int(input("Enter a board size: "))


# Set first item in row to 1 
nth_row = [[1]]
for x in range(n-1): # Append 0 to reach value of n 
    nth_row[0].append(0)

for i in range(1,n): # For each new row create new list & append 1 as the beginning number
    nth_row.append([1]) 
    for j in range(1,i): # Iteratre through previous row and add adjacent numbers
        nth_row[i].append(nth_row[i-1][j-1] + nth_row[i-1][j])
    nth_row[i].append(1) # Append 1 to the very end
    
    for k in range(n):
        if len(nth_row[i]) < n: # If length of current list less than n ; Append 0 to fill up board
            nth_row[i].append(0)

# Print rows and columns
for board in nth_row:
    print(*board)