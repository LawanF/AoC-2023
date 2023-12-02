# Extract max values for blue, red, and green from the input for each game, 
# then simply compare the max values to the limits given in the spec
import time

start_time = time.time()

input = open("./input.txt", "r").read().split("\n")

red_lim = 12
green_lim = 13
blue_lim = 14

ans1 = 0
ans2 = 0

# stripping down input
inputMod1 = [s[s.index(":") + 2:].split("; ") for s in input]

for gameInd in range(0, len(inputMod1)):

    # rearranging the data into a more easy-to-work-with format
    val_cols = [s.split(", ") for s in inputMod1[gameInd]]
    flat_val_cols = [a for b in val_cols for a in b]

    # now we have tuples of the shape ("3", "red")
    tuple_val_cols = [tuple(s.split(" ")) for s in flat_val_cols]

    # keeping track of the highest number of cubes seen
    red_max = 0
    green_max = 0
    blue_max = 0
    
    
    # checking if the shown cube exceeds the previous max shows
    for i in tuple_val_cols:
        match i[1]: # matching for correct colours
            case "red":
                if int(i[0]) > red_max:
                    red_max = int(i[0])

            case "green":
                if int(i[0]) > green_max:
                    green_max = int(i[0])
            
            case "blue":
                if int(i[0]) > blue_max:
                    blue_max = int(i[0])
        
    # if none exceeds max, add gameID to ans1
    if red_max <= red_lim and green_max <= green_lim and blue_max <= blue_lim:
        ans1 += gameInd + 1
    
    # add power of sets to answer 2
    ans2 += red_max * green_max * blue_max

print("Answer for part 1 is: " + str(ans1) + ".")
print("Answer for part 2 is: " + str(ans2) + ".")

end_time = time.time()

print("Runtime is: " + str(round(end_time - start_time, 5) * 1000) + " miliseconds.")

