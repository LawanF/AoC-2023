import timeit
start_time = timeit.default_timer()

input = open("input4.txt", "r").read().splitlines()

# --- PARSING INPUT ---

# removing the first part of the string, the "Card {Num}".
# splitting input into two different strings, one for winning numbers, 
# one for scratch numbers 
inputMod1 = [s.split(":")[1].split("|") for s in input]
# format is [winning_numbers, numbers]



inputMod3 = []
for line in inputMod1:
    win = [s for s in line[0].split(" ") if s != ""]
    num = [s for s in line[1].split(" ") if s != ""]
    inputMod3.append([1, win, num])
# Input is now in format [number_of_card, [winning_numbers], [numbers]] for each line.

def part1():
    ans1 = 0


    for card in inputMod3:
        curPts = 0

        for num in card[2]:
            # if number is in the winning number, 
            # increase points as necessary
            if num in card[1]:
                if curPts == 0:
                    curPts = 1
                else:
                    curPts *= 2
        ans1 += curPts
    return ans1

def part2():
    ans2 = 0
    for lineInd in range(0, len(inputMod3)):
        num_matches = 0
        for num in inputMod3[lineInd][2]:
            if num in inputMod3[lineInd][1]:
                num_matches += 1

        for i in range(1, num_matches + 1):
            inputMod3[lineInd + i][0] += inputMod3[lineInd][0]
        ans2 += inputMod3[lineInd][0]
    return ans2

print(f"Answer to part 1 is: {part1()}.") # look up f strings later
print(f"Answer to part 2 is: {part2()}.")

end_time = timeit.default_timer() - start_time

print(f"Runtime is: {end_time * 1000:.5f} miliseconds.")

