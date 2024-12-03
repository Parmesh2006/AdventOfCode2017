from collections import deque
from functools import reduce
from operator import xor

in_str_prefix = 'jxqlasbh'

def knot_hash_list(lengths, cycle_size=256, iterations=64):
    seq = deque(range(cycle_size))
    skip = 0

    for _ in range(iterations):
        for l in lengths:
            seq.extend(reversed(deque(seq.popleft() for _ in range(l))))
            seq.rotate(-skip)
            skip += 1

    seq.rotate(iterations * sum(lengths) + skip * (skip-1) // 2)
    seq = list(seq)
    return [reduce(xor, seq[i:i + 16]) for i in range(0, cycle_size, 16)]

def str_to_lengths(s, extend=()): 
    return [ord(x) for x in s] + list(extend)

rows = []
for i in range(128):
    lengths = str_to_lengths(f'{in_str_prefix}-{i}', extend=[17, 31, 73, 47, 23])
    dense = knot_hash_list(lengths)
    st = ''.join(f'{x:08b}' for x in dense)
    rows.append([int(x) for x in st])

def wipe_region(r, c):
    if r < 0 or c < 0 or r >= len(rows) or c >= len(rows[r]) or rows[r][c] == 0: 
        return 0
    
    rows[r][c] = 0
    wipe_region(r+1, c)
    wipe_region(r, c+1)
    wipe_region(r-1, c)
    wipe_region(r, c-1)
    
    return 1

print(f"PART 1: {sum(sum(x) for x in rows)}")
print(f"PART 2: {sum(wipe_region(j, i) for j in range(len(rows)) for i in range(len(rows[j])))}")