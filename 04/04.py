lists = [line.strip() for line in open("input").readlines()]

number_of_rows = len(lists)
number_of_columns = len(lists[0])
number_of_diagonals = number_of_columns + number_of_rows - 1

horizontals = lists
verticals = ["" for _ in lists[0]]
topleft_bottomright_diags = ["" for _ in range(number_of_diagonals)]
topright_bottomleft_diags = ["" for _ in range(number_of_diagonals)]

for i, l in enumerate(lists):
    for j, character in enumerate(l):
        verticals[j] += character
        try:
            topleft_bottomright_diags[i - j] += character
        except IndexError:
            pass
        try:
            topright_bottomleft_diags[i + j] += character
        except IndexError:
            pass

hits = 0
for word in ["XMAS", "SAMX"]:
    for line in (
        horizontals + verticals + topleft_bottomright_diags + topright_bottomleft_diags
    ):
        hits += line.count(word)

print(hits)


def process(x, y):
    new_hits = 0
    try:
        horizontal_mas = lists[x - 1][y] == "M" and lists[x + 1][y] == "S"
        horizontal_sam = lists[x - 1][y] == "S" and lists[x + 1][y] == "M"
    except IndexError:
        horizontal_sam = False
        horizontal_mas = False

    try:
        vertical_mas = lists[x][y - 1] == "M" and lists[x][y + 1] == "S"
        vertical_sam = lists[x][y - 1] == "S" and lists[x + 1][y] == "M"
    except IndexError:
        vertical_mas = False
        vertical_sam = False

    try:
        diag1_mas = lists[x - 1][y - 1] == "M" and lists[x + 1][y + 1] == "S"
        diag1_sam = lists[x - 1][y - 1] == "S" and lists[x + 1][y + 1] == "M"
    except IndexError:
        diag1_mas = False
        diag1_sam = False

    try:
        diag2_mas = lists[x - 1][y + 1] == "M" and lists[x + 1][y - 1] == "S"
        diag2_sam = lists[x - 1][y + 1] == "S" and lists[x + 1][y - 1] == "M"
    except IndexError:
        diag2_mas = False
        diag2_sam = False

    horizontal = horizontal_sam or horizontal_mas
    vertical = vertical_sam or vertical_mas
    diag1 = diag1_sam or diag1_mas
    diag2 = diag2_sam or diag2_mas

    straight_cross = horizontal and vertical

    st_andrews_cross = diag1 and diag2

    # if straight_cross:
    #     new_hits +=1
    if st_andrews_cross:
        new_hits += 1
    if new_hits > 1:
        print(x, y, new_hits)
        print([lists[x - 1][y - 1], lists[x][y - 1], lists[x + 1][y - 1]]),
        print([lists[x - 1][y], lists[x][y], lists[x + 1][y]])
        print([lists[x - 1][y + 1], lists[x][y + 1], lists[x + 1][y + 1]])
    return new_hits


mas_count = 0
for i, line in enumerate(lists):
    for j, character in enumerate(line):
        if character == "A":
            new_hits = process(i, j)
            mas_count += new_hits

print(mas_count)
