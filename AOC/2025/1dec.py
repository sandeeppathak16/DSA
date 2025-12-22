with open('1dec.txt') as file:
    codes = [line.strip() for line in file if line.strip()]

initial_point = 50


def calculate_final_position(codes, initial_position):
    position = initial_position
    res = 0

    for code in codes:
        direction = code[0]
        value = int(code[1:])

        if value >= 100:
            value %= 100

        if direction == 'L':
            position -= value

            if position < 0:
                position += 100

        elif direction == 'R':
            position += value

            if position >= 100:
                position -= 100

        if position == 0:
            res += 1

    return res, position


def calculate_final_position_2(codes, initial_position):
    position = initial_position
    res = 0

    for code in codes:
        direction = code[0]
        value = int(code[1:])

        if value >= 100:
            res += (value // 100)
            value %= 100

        prev_position = position
        if direction == 'L':
            position -= value

            if position < 0:
                position += 100

            if prev_position != 0 and prev_position < position:
                res += 1
            elif position == 0:
                res += 1

        elif direction == 'R':
            position += value

            if position >= 100:
                position -= 100

            if prev_position != 0 and prev_position > position:
                res += 1
            elif position == 0:
                res += 1

    return res, position


print(calculate_final_position(codes, initial_position=initial_point))
print(calculate_final_position_2(codes, initial_position=initial_point))
