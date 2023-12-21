import math
import timeit

start_time = timeit.default_timer()

# --- PARSING INPUT ---
inp = open("input8.txt", "r").read().splitlines()

rl_inst = inp[0]
rl_len = len(rl_inst)
inpMod1 = [i.split(" = ") for i in inp[2:]]
print(inpMod1)

des_map = {}

for i in inpMod1:
    b = i[1][1:-1]
    x, y = b.split(", ")
    des_map[i[0]] = (x, y)
# Counting steps
def part1():
    curPos = "AAA"
    rl_i = 0
    steps = 0
    
    while curPos != "ZZZ":
        steps += 1
        if rl_i == rl_len:
            rl_i = 0
        if rl_inst[rl_i] == "L":
            curPos = des_map[curPos][0]
        else:
            curPos = curPos = des_map[curPos][1]
        rl_i += 1

    return steps

def part2():

    positions = [i[0] for i in inpMod1 if i[0][-1] == "A"]
    allStep = []
    for curPos in positions:
        steps = 0
        rl_i = 0

        while curPos[-1] != "Z":
            steps += 1

            if rl_i == rl_len:
                rl_i = 0
            if rl_inst[rl_i] == "L":
                curPos = des_map[curPos][0]
            else:
                curPos = des_map[curPos][1]
            rl_i += 1

        allStep.append(steps)
    
    def lcm_list(xs):
        l = 1
        for j in range(0, len(xs)):
            l = math.lcm(l, xs[j])
        return l

    return lcm_list(allStep)

print(f"Answer to part 1 is: {part1()}.") # look up f strings later
print(f"Answer to part 2 is: {part2()}.")

end_time = timeit.default_timer() - start_time

print(f"Runtime is: {end_time * 1000:.5f} miliseconds.")