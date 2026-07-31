def solve(filename="20.txt"):
    with open(filename) as f:
        ranges = [
            tuple(map(int, line.split("-")))
            for line in f
            if line.strip()
        ]

    if not ranges:
        return 0

    ranges.sort()

    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    MAX_IP = 2**32 - 1

    current_ip = 0
    first_valid_ip = None
    valid_count = 0

    for blocked_start, blocked_end in merged:
        if current_ip < blocked_start:
            if first_valid_ip is None:
                first_valid_ip = current_ip

            valid_count += blocked_start - current_ip

        current_ip = blocked_end + 1

        if current_ip > MAX_IP:
            break

    if current_ip <= MAX_IP:
        if first_valid_ip is None:
            first_valid_ip = current_ip

        valid_count += MAX_IP - current_ip + 1

    return first_valid_ip, valid_count