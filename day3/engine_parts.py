# --- this code works with non-rectangular schematics!

import re
import time

start_time = time.time()

input = open("input3.txt", "r").read().splitlines()
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
ans1 = 0
ans2 = 0

# split on everything except numbers to extract the numbers
numExtracted = [re.split('[^0-9]', s) for s in input]

# number indices in the format (number, row, start_column, end_column)
numInds = []

# grab number indices
for i in range(0, len(numExtracted)):
    curCol = 0

    for j in range(0, len(numExtracted[i])):
        # skip empty strings
        if numExtracted[i][j] != '':
            numInds.append((int(numExtracted[i][j]), i, curCol, curCol + len(numExtracted[i][j]) - 1))
            curCol += len(numExtracted[i][j]) # adjust column number by the length of the number

        curCol += 1


# grab symbol indices in the format (row, column)
symbInds = [(s, i) for s in range (0, len(input)) for i in range(0, len(input[s])) if input[s][i] not in numbers and input[s][i] != '.']
# keeping track of filtered numbers
filteredNums = []

# grab numbers that are adjacent to symbols
for symb in symbInds:
    x, y = symb
    adjNums = [] # keep track of adjacent numbers for current symbol

    for numInf in numInds:
        num, row, start_col, end_col = numInf

        # if current number is adjacent to symbol, add to filteredNums and adjNums
        if abs(row - x) <= 1 and (abs(start_col - y) <= 1 or abs(end_col - y) <= 1):
            filteredNums.append(num)
            adjNums.append(num)
    
    # if the number of adjacent numbers is exactly 2, add the gear ratio to ans2
    if len(adjNums) == 2:
        ans2 += adjNums[0] * adjNums[1]


ans1 = sum(filteredNums)

print("Answer to part 1 is: " + str(ans1) + ".")
print("Answer to part 2 is: " + str(ans2) + ".")

end_time = time.time()

print("Runtime is: " + str(round(end_time - start_time, 5) * 1000) + " miliseconds.")