with open('9.txt', 'r') as file:
    line = [line.strip() for line in file.readlines()][0]
    line = list(line)


represents = []

# space = False
# file_id = 0
#
# for ele in line:
#     if space:
#         represent = ['.']
#     else:
#         represent = [str(file_id)]
#         file_id += 1
#
#     space = not space
#     represents.extend(represent * int(ele))
#
#
# n = len(represents)
# l_index_space = None
# r_file_index = None
#
# for i, ele in enumerate(represents):
#     if ele == '.':
#         if l_index_space is None:
#             l_index_space = i
#     else:
#         r_file_index = i
#
# i = l_index_space
# j = r_file_index
#
# while j > i:
#     while i < n and represents[i] != '.':
#         i += 1
#
#     while j >= 0 and represents[j] == '.':
#         j -= 1
#
#     if i < n and j >= 0 and j > i:
#         represents[i], represents[j] = represents[j], represents[i]
#
#         i += 1
#         j -= 1
#
#
# ans1 = 0
#
# for indx, ele in enumerate(represents):
#     if ele == '.':
#         continue
#
#     ans1 += (indx * int(ele))
#
# print(ans1)

# files = []
# spaces = []
#
# is_space = False
# file_id = 0
#
# for ch in line:
#     length = int(ch)
#
#     if not is_space:
#         files.append([len(represents), length, file_id])
#         represents.extend([str(file_id)] * length)
#         file_id += 1
#     else:
#         spaces.append([len(represents), length])
#         represents.extend(['.'] * length)
#
#     is_space = not is_space
#
#
# for fid in range(file_id - 1, -1, -1):
#
#     for i in range(len(represents)):
#         if represents[i] == str(fid):
#             file_start = i
#             break
#
#     file_len = represents.count(str(fid))
#
#     space_start = None
#     space_len = 0
#
#     i = 0
#     while i < file_start:
#         if represents[i] == '.':
#             j = i
#             while j < len(represents) and represents[j] == '.':
#                 j += 1
#             if j - i >= file_len:
#                 space_start = i
#                 space_len = j - i
#                 break
#             i = j
#         else:
#             i += 1
#
#     if space_start is None:
#         continue
#
#     for i in range(file_len):
#         represents[space_start + i] = str(fid)
#
#     for i in range(file_start, file_start + file_len):
#         represents[i] = '.'
#
#
# # print(represents)
#
# ans1 = 0
#
# for indx, ele in enumerate(represents):
#     if ele == '.':
#         continue
#
#     ans1 += (indx * int(ele))
#
# print(ans1)


def solve_part2_optimized(line):
    disk = []
    file_id = 0
    is_file = True

    for ch in line:
        length = int(ch)
        if is_file:
            disk.append(["file", file_id, length])
            file_id += 1
        else:
            disk.append(["space", None, length])
        is_file = not is_file

    for fid in range(file_id - 1, -1, -1):

        for i, seg in enumerate(disk):
            if seg[0] == "file" and seg[1] == fid:
                file_idx = i
                file_len = seg[2]
                break

        for j in range(file_idx):
            if disk[j][0] == "space" and disk[j][2] >= file_len:
                space_len = disk[j][2]

                disk[j] = ["file", fid, file_len]

                if space_len > file_len:
                    disk.insert(j + 1, ["space", None, space_len - file_len])
                    if j < file_idx:
                        file_idx += 1

                disk[file_idx] = ["space", None, file_len]
                break

    checksum = 0
    pos = 0
    for seg in disk:
        if seg[0] == "file":
            fid = seg[1]
            for _ in range(seg[2]):
                checksum += pos * fid
                pos += 1
        else:
            pos += seg[2]

    return checksum


print(solve_part2_optimized(line))








