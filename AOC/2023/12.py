from functools import lru_cache

def count_arrangements(pattern, groups):
    n = len(pattern)
    groups = tuple(groups)

    @lru_cache(None)
    def dfs(i, gi, run):
        """
        i  = current index in pattern
        gi = index of current group
        run = current length of consecutive '#'
        """

        # End of pattern
        if i == n:
            if gi == len(groups) and run == 0:
                return 1
            if gi == len(groups) - 1 and run == groups[gi]:
                return 1
            return 0

        total = 0
        ch = pattern[i]

        # Try placing '.'
        if ch in '.?':
            if run == 0:
                total += dfs(i + 1, gi, 0)
            elif gi < len(groups) and run == groups[gi]:
                total += dfs(i + 1, gi + 1, 0)

        # Try placing '#'
        if ch in '#?':
            if gi < len(groups) and run < groups[gi]:
                total += dfs(i + 1, gi, run + 1)

        return total

    return dfs(0, 0, 0)


total = 0
part2 = True

with open("12.txt") as f:
    for line in f:
        pattern, nums = line.strip().split()
        groups = list(map(int, nums.split(",")))
        if part2:
            pattern = "?".join([pattern] * 5)
            groups = groups * 5
        total += count_arrangements(pattern, groups)

print(total)
