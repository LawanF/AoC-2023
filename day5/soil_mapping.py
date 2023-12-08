import timeit
start_time = timeit.default_timer()

input = open("input5.txt", "r").read().splitlines()
# print(input)
def part1():
    # --- PARSING INPUT ---
    # Grab seeds
    seeds = input[0].split(":")[1][1:]
    # print(seeds)

    # getting# rid of unnecessary information
    inputMod1 = [s for s in input[2:] if s[-1:] != ":"]

    inputMod2 = []
    splicer = 0
    for i in range(0, len(inputMod1)):
        if inputMod1[i] == "":
            inputMod2.append(inputMod1[splicer:i])
            splicer = i + 1
    inputMod2.append(inputMod1[splicer:])

    def nums_to_ranges(s):
        if s == "":
            return s
        split_s = s.split(" ")
        start_integer = [int(i) for i in split_s]
        return [range(start_integer[0], start_integer[0] + start_integer[2]), range(start_integer[1], start_integer[1] + start_integer[2])]

    inputMod3 = [[nums_to_ranges(i) for i in s] for s in inputMod2]
    # input is now in the form [[(dest1, source1), (dest2, source2), ...], ...]

    mapping = [[int(s)] for s in seeds.split()]

    def rangeMap(source_map, map_ranges):
        result = []
        for m in source_map:
            res_ap = m[-1]
            for r in map_ranges:
                if res_ap in r[1]:
                    res_ap = r[0][r[1].index(res_ap)]
                    break
            result.append(res_ap)
        
        return result

    for line in inputMod3:
        appendices = rangeMap(mapping, line)
        for i in range(0, len(mapping)):
            mapping[i].append(appendices[i])

            
    loc_numbers = [s[-1] for s in mapping]
    print(min(loc_numbers))

seeds = input[0].split(":")[1][1:].split(" ")
seed_ranges = []
for i in range(0, len(seeds)//2 + 1, 2):
    start, length = (seeds[i], seeds[i + 1])
    seed_ranges.append((int(start), int(start) + int(length)))
# format is [(start, end)]

inputMod1 = [s for s in input[2:] if s[-1:] != ":"]

def string_to_range(s):
    if s == "":
        return s
    else:
        dest, sour, size = [int(i) for i in s.split(" ")]
        return [(dest, dest + size), (sour, sour + size)]

inputMod2 = [string_to_range(s) for s in inputMod1]
print(inputMod2)
# format is [[(start, end)]]

end_time = timeit.default_timer()
print(end_time - start_time)



