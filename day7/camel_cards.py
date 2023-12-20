import enum
import timeit

start_time = timeit.default_timer()
# --- PARSING INPUT ---
inp = open('input7.txt', 'r').read().splitlines()

split = [i.split(" ") for i in inp]

hands = [i[0] for i in split]
bids = [i[1] for i in split]

card_values = {
    'A' : 12,
    'K' : 11,
    'Q' : 10,
    'J' : 9,
    'T' : 8,
    '9' : 7, 
    '8' : 6, 
    '7' : 5,
    '6' : 4, 
    '5' : 3,
    '4' : 2,
    '3' : 1,
    '2' : 0
}

hand_values = {
    '5oK' : 6,
    '4oK' : 5,
    'FH' : 4,
    '3oK' : 3,
    '2P' : 2,
    '1P' : 1,
    'HC' : 0
}

def sort_hand_1():
    h_info = []
    for ind, h in enumerate(hands):
        c_count = [0 for _ in range(0, card_values['A'] + 1)]
        b = bids[ind]
        val = 'HC'
        for c in h:
            c_count[card_values[c]] += 1

        if 5 in c_count:
            val = '5oK'
        elif 4 in c_count:
            val = '4oK'
        elif 3 in c_count and 2 in c_count:
            val = 'FH'
        elif 3 in c_count:
            val = '3oK'
        elif 2 in c_count:
            c_count.remove(2)
            if 2 in c_count:
                val = '2P'
            else:
                val = '1P'
        
        h_info.append(val)
    return h_info

def sort_hand_2():
    h_info = []
    for ind, h in enumerate(hands):
        c_count = [0 for _ in range(0, card_values['A'] + 1)]
        b = bids[ind]
        val = 'HC'
        j_count = 0
        for c in h:
            if c == 'J':
                j_count += 1
            else:
                c_count[card_values[c]] += 1
        
        c_count[c_count.index(max(c_count))] = max(c_count) + j_count

        if 5 in c_count:
            val = '5oK'
        elif 4 in c_count:
            val = '4oK'
        elif 3 in c_count and 2 in c_count:
            val = 'FH'
        elif 3 in c_count:
            val = '3oK'
        elif 2 in c_count:
            c_count.remove(2)
            if 2 in c_count:
                val = '2P'
            else:
                val = '1P'
        
        h_info.append(val)
    return h_info

# Replaces J

# Returns true if hand a <= hand b, "lexicographically"
def is_smaller_lex(a_ind, b_ind):
    for c_ind, a_c in enumerate(hands[a_ind]):
        b_c = hands[b_ind][c_ind]
        if card_values[a_c] < card_values[b_c]:
            return True
        if card_values[a_c] > card_values[b_c]:
            return False
# Returns true if hand a < hand b, given their indices in hands
def is_smaller(a_ind, b_ind):
    a_v = hand_values[hand_info[a_ind]]
    b_v = hand_values[hand_info[b_ind]]
    if a_v < b_v:
        return True
    if a_v == b_v:
        return is_smaller_lex(a_ind, b_ind)
    else:
        return False

def insert_sort(h_ind, l):
    if l == []:
        return [h_ind]
    elif is_smaller(h_ind, l[0]):
        return [h_ind] + l
    else:
        return l[0:1] + insert_sort(h_ind, l[1:])

def part1():
    card_values['A'] = 12
    card_values['K'] = 11
    card_values['Q'] = 10
    card_values['J'] = 9
    sort_hand_1()
    results = []
    for h in range(0, len(hands)):
        results = insert_sort(h, results)

    bid_results = [int(bids[results[i]]) * (i + 1) for i in range(0, len(results))]
    return sum(bid_results)

def part2():
    card_values['A'] = 11
    card_values['K'] = 10
    card_values['Q'] = 9
    card_values['J'] = -1

    sort_hand_2()
    results = []
    for h in range(0, len(hands)):
        results = insert_sort(h, results)

    bid_results = [int(bids[results[i]]) * (i + 1) for i in range(0, len(results))]
    return sum(bid_results)



hand_info = sort_hand_1()
print(f"Answer to part 1 is: {part1()}.") # look up f strings later

hand_info = sort_hand_2()
print(f"Answer to part 2 is: {part2()}.")

end_time = timeit.default_timer() - start_time

print(f"Runtime is: {end_time * 1000:.5f} miliseconds.")

