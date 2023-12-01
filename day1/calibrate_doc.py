import time

start_time = time.time()

input = open("input1.txt", "r").read().split("\n")

listOfNums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
listOfStrNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
listOfRevNums = [i[::-1] for i in listOfStrNums]

answer = []

for lineInd in range(0, len(input)):
    curLine = input[lineInd]

    # iterate through string from the beginning
    for c in range(0, len(curLine)):
        # if current character is a number, append it to answer
        if curLine[c] in listOfNums:
            answer.append(int(curLine[c]) * 10)
            break
        
        curSubstr = curLine[0:(c + 1)]
        # check if any written number is in substring
        check = [(listOfStrNums.index(s) + 1) for s in listOfStrNums if s in curSubstr]
        # if anything matches, append it to answer
        if check:
            answer.append(check[0] * 10)
            break
    
    # iterate through string from the end
    for c in range(1, len(curLine) + 1):
        # if current character is a number, add it to the relevant index in answer
        if curLine[-c] in listOfNums:
            answer[lineInd] += (int(curLine[-c]))
            break

        curSubstr = curLine[-1:(-c - 1):-1]
        # once again, check for written out numbers, but in reverse
        check = [(listOfRevNums.index(s) + 1) for s in listOfRevNums if s in curSubstr]
        # if one exists, add it to the relevant index in answer
        if check:
            answer[lineInd] += check[0]
            break

finAnswer = sum(answer)

print("Answer is " + str(finAnswer) + ".")

end_time = time.time()

print("Runtime is: " + str(round(end_time - start_time, 5)) + " seconds.")