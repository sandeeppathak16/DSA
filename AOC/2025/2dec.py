with open('2dec.txt', 'r') as f:
    content = f.read()
    codes = [code.strip() for code in content.split(',') if code.strip()]


def sum_invalid_ids_in_ranges(ranges, invalid_ids):
    total = 0
    i = 0

    for val in invalid_ids:
        while i < len(ranges) and val > ranges[i][1]:
            i += 1

        if i == len(ranges):
            break

        if ranges[i][0] <= val <= ranges[i][1]:
            total += 1

    return total


def generate_invalid_ids(global_min, global_max):
    invalid_ids = []

    min_len = len(str(global_min))
    max_len = len(str(global_max))

    for total_len in range(min_len, max_len + 1):
        if total_len % 2 != 0:
            continue

        half_len = total_len // 2
        start_seed = 10 ** (half_len - 1)
        end_seed = 10 ** half_len - 1

        for seed in range(start_seed, end_seed + 1):
            s = str(seed)
            candidate = int(s + s)

            if candidate > global_max:
                break

            if candidate < global_min:
                break

            invalid_ids.append(candidate)

    return sorted(invalid_ids)


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_start + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return [(s, e) for s, e in merged]


ans = 0


def find_invalid_number(n1, n2):
    global ans

    for number in range(n1, n2 + 1):
        str_number = str(number)
        len_number = len(str_number)

        for i in range(1, len_number):
            sub_set = []
            j = 0
            k = i

            while k < len_number + i:
                sub_set.append(int(str_number[j:k]))
                j = k
                k += i

            is_valid = True

            for z in range(len(sub_set) - 1):
                if sub_set[z] != sub_set[z + 1]:
                    is_valid = False
                    break

            if is_valid:
                ans += number
                break

ans = 0
ranges = []
for code in codes:
    n1, n2 = map(int, code.split('-'))
    find_invalid_number(n1, n2)
    ranges.append([n1, n2])


print(ans)

merged_ranges = merge_ranges(ranges)
global_min = min(s for s, _ in merged_ranges)
global_max = max(s for s, _ in merged_ranges)

invalid_ids = generate_invalid_ids(global_min, global_max)
answer = sum_invalid_ids_in_ranges(merged_ranges, invalid_ids)