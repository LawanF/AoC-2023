# t = race time
# b = button hold time
# d = distance
# r = current record
# d = (t - b) * b = bt - b^2
# we want d > r
# bt - b^2 > r
# b^2 - bt + r < 0
# t/2 - sqrt((t/2)^2 - r) < b < t/2 + sqrt((t/2)^2 - r)
import timeit
import math

start_time = timeit.default_timer()

# --- PARSING INPUT ---
inp = open("input6.txt", "r").read().splitlines()
times = inp[0].split()[1:]
records = inp[1].split()[1:]


# We will simply solve the inequality above for b, and then round these
# boundaries appropriately. This is done using find_bounds()

# function to find bounds of inequality
def find_bounds(t, r):
    return (t/2 - ((t/2) ** 2 - r) ** (1/2), t/2 + ((t/2) ** 2 - r) ** (1/2))

def part1():
    
    
    ways = []
    for ind, t_str in enumerate(times):
        t = int(t_str)
        r = int(records[ind])
        low, high = find_bounds(t, r)

        # we append the number of ways to ways
        ways.append(math.trunc(high) - math.ceil(low) + 1)
        # high bound is truncated as it has to be lower to be quicker
        # we use ceiling on low bound because it has to be higher
    
    result = 1
    for w in ways:
        result *= w
    
    return result
    

def part2():
    # further parsing of input
    time = ""
    record = ""
    for t in times:
        time += t
    for r in records:
        record += r
    time = int(time)
    record = int(record)

    # applying the same principle, but only for the one race
    low, high = find_bounds(time, record)
    return math.trunc(high) - math.ceil(low) + 1

print(f"Answer to part 1 is: {part1()}.") # look up f strings later
print(f"Answer to part 2 is: {part2()}.")

end_time = timeit.default_timer() - start_time

print(f"Runtime is: {end_time * 1000:.5f} miliseconds.")






