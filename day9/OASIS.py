import math
import timeit

start_time = timeit.default_timer()

# --- PARSING INPUT ---
inp = open("input9.txt", "r").read().splitlines()
seq_list = [i.split() for i in inp]
seq_list = [[int(j) for j in i] for i in seq_list]

# Function to get the sequence of differences
def sub_seq(xs):
    return [xs[i] - xs[i - 1] for i in range(1, len(xs))]

# Function to check if all elements of a list are zeros
def all_zeros(xs):
    for x in xs:
        if x != 0:
            return False
    return True

# Function to take sub_seq until you get a list of all zeros
# Then return all of those sub sequences
def until_zeros(xs):
    res = [xs]
    while not all_zeros(res[-1]):
        res.append(sub_seq(res[-1]))
    return res

# Function to extrapolate value forwards, given the full sequence
# of sub sequences.
def next_val(ys_xs):
    n = 0
    for i in range(len(ys_xs) - 1, 0, -1):
        b = ys_xs[i - 1][-1]
        n = b + n
    return n

# Function to extrapolate backwards
def prev_val(ys_xs):
    n = 0
    for i in range(len(ys_xs) - 1, 0, -1):
        b = ys_xs[i - 1][0]
        n = b - n
    return n

def part1():
    ans = 0
    for seq in seq_list:
        ans += next_val(until_zeros(seq))
    return ans

def part2():
    ans = 0
    for seq in seq_list:
        ans += prev_val(until_zeros(seq))

    return ans
        
print(f"Answer to part 1 is: {part1()}.") # look up f strings later
print(f"Answer to part 2 is: {part2()}.")

end_time = timeit.default_timer() - start_time

print(f"Runtime is: {end_time * 1000:.5f} miliseconds.")        
