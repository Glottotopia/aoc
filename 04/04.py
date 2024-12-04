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
