def main(problem_input: list[str]):
    
    seed, *others = problem_input
    seed = [int(x) for x in seed.split(":")[1].split()]
    
    def process(mapping):
        lines = mapping.split("\n")[1:]  
        tuples: list[tuple[int, int, int]] = [
            [int(x) for x in line.split()] for line in lines
        ]
        return tuples
    
    def apply_part_one(x, mapping):
        for dst, src, sz in process(mapping):
            if src <= x < src + sz:
                return x + dst - src
        return x
    
    def apply_part_two(r, mapping):
        A = []
        for dst, src_start, sz in process(mapping):
            src_end = src_start + sz
            NR = []
            while r:
                (start, end) = r.pop()
                before = (start, min(end, src_start))
                inter = (max(start, src_start), min(src_end, end))
                after = max(src_end, start), end
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] + dst - src_start, inter[1] + dst - src_start))
                if after[1] > after[0]:
                    NR.append(after)
            r = NR
        return A + r    
    
    part_one = []
    for x in seed:
        for other in others:
            x = apply_part_one(x, other)
        part_one.append(x) 
        
    part_two = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for start_seed, size_range in pairs:
        seed_range = [(start_seed, start_seed + size_range)] 
        for other in others:
            seed_range = apply_part_two(seed_range, other)
        part_two.append(min(seed_range)[0])
    
    return min(part_one), min(part_two)