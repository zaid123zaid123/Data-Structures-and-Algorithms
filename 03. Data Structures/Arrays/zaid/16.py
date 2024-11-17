# import random
# matrix = []
# total = 0
# numberOfRows = eval(input("Enter the number of rows: "))
# numberOfColumns = eval(input("Enter the number of columns: "))
# for row in range(0, numberOfRows): 
#     matrix.append([])
#     for column in range(0, numberOfColumns):
#         matrix[row].append(random.randrange(0, 100)) 
#         total += matrix[ row][column]
#         total co
# print(matrix)  
# print("Total is " + str(total)) # Print the total  
    # Students' answers to the questions

# def main():
#     # Students' answers to the questions
#     answers = [
#       ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
#       ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
#       ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
#       ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
#       ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
#       ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
#       ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
#       ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
      
#     # Key to the questions
#     keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    
#     # Grade all answers
#     for i in range(len(answers)):
#         # Grade one student
#         correctCount = 0
#         for j in range(len(answers[i])): 
#             if answers[i][j] == keys[j]:
#                 correctCount += 1

#         print("Student", i, "'s correct count is", correctCount)

# main() # Call the main function



# Check whether a solution is valid 
def isValid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 1 or grid[i][j] > 9 \
               or not isValidAt(i, j, grid):
                return False
    return True # The fixed cells are valid

# Check whether grid[i][j] is valid in the grid 
def isValidAt(i, j, grid):
    # Check whether grid[i][j] is valid at the i's row
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid at the j's column
    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid in the 3 by 3 box
    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
          for col in range((j // 3) * 3, (j // 3) * 3 + 3):
             if row != i and col != j and \
                    grid[row][col] == grid[i][j]:
                 return False

    return True # The current value at grid[i][j] is valid