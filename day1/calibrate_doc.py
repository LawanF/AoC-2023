input = open("input1.txt", "r").read().split("\n")
listOfNums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
listOfStrNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
listOfRevNums = [i[::-1] for i in listOfStrNums]
answer = []


for lineInd in range(0, len(input)):
    curLine = input[lineInd]

    
    for c in range(0, len(curLine)):
        # if current character is a number, append it to answer
        if curLine[c] in listOfNums:
            print(curLine[c])
            answer.append(int(curLine[c]) * 10)
            break
        
        curSubstr = curLine[0:(c + 1)]
        check = [(10 * (listOfStrNums.index(s) + 1)) for s in listOfStrNums if s in curSubstr]
        if check:
            answer.append(check[0])
            break
    
    for c in range(1, len(curLine) + 1):
        if curLine[-c] in listOfNums:
            answer[lineInd] += (int(curLine[-c]))
            break

        curSubstr = curLine[-1:(-c - 1):-1]
        check = [(listOfRevNums.index(s) + 1) for s in listOfRevNums if s in curSubstr]
        if check:
            answer[lineInd] += check[0]
            break
        


print(answer)

finAnswer = sum(answer)

print(finAnswer)