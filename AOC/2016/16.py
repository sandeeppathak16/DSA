def check_sum(bits):
    if len(bits) % 2 == 1:
        return bits

    new_bits = ""

    for i in range(0, len(bits), 2):
        if bits[i] == bits[i + 1]:
            new_bits += "1"
        else:
            new_bits += "0"

    return check_sum(new_bits)


def solve(bits, disc_length):
    while len(bits) < disc_length:
        bits_copy = bits[::-1]
        flipped_copy = "".join(
            "1" if b == "0" else "0"
            for b in bits_copy
        )
        bits = bits + "0" + flipped_copy

    bits = bits[:disc_length]
    return check_sum(bits)


print(solve("11110010111001001", 35651584))