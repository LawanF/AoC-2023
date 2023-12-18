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
for i in range(0, len(seeds), 2):
    start, length = (seeds[i], seeds[i + 1])
    seed_ranges.append((int(start), int(start) + int(length)))
# format is [(start, end)]

inputMod1 = [s for s in input[2:] if s[-1:] != ":"]


def string_to_range(s):
    if s == "":
        return s
    else:
        dest, sour, size = [int(i) for i in s.split(" ")]
        return [(dest, dest + size - 1), (sour, sour + size - 1)]

inputMod2 = [string_to_range(s) for s in inputMod1]

inputMod3 = []
res1 = []
for i in inputMod2:
    if i == '':
        inputMod3.append(res1)
        res1 = []
    else:
        res1 += i
inputMod3.append(res1)
print(inputMod3)
# format is [[(s_start, s_end), (d_start, d_end), ...], ...]

mapping = [[s] for s in seed_ranges]
print(mapping)

# finds and returns overlap and residual range from two ranges
# for overlap, maps to d_r
# format is (res1, res2, mapped_range)
def map_rest(m_r, d_r, s_r):
    m_start, m_end = m_r
    s_start, s_end = s_r
    d_start, d_end = d_r
    shift = s_start - d_start
    o_start = max(m_start, s_start)
    o_end = min(m_end, s_end)
    if o_end < o_start:
        return (m_r, None, None)
    elif m_start < o_start and o_end < m_end:
        return ((m_start, o_start), (o_end, m_end), (o_start, o_end))
    elif o_start <= m_start and o_end < m_end:
        return (None, (o_end, m_end), (o_start, o_end))
    elif m_start < o_start and m_end < o_end:
        return((m_start, o_start), None, (o_start, o_end))
    

for l_ind, line in enumerate(inputMod3):
    for m_list in mapping:
        m_start, m_end = m_list[-1] 
        for d_ind in range(0, len(line), 2):
            


        


# end_time = timeit.default_timer()
# print(end_time - start_time)



