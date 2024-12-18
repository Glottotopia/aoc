import math
import pprint
import copy


def get_deltas(l):
    result = []
    for i in range(1, len(l)):
        result.append(l[i] - l[i - 1])
    return result


def evaluate_deltas(deltas):
    signs = {math.copysign(1, x) for x in deltas}
    if len(signs) != 1:  # there is either no sign, or both + and -
        return False
    if 0 in deltas:
        return False
    if max(deltas) > 3:
        return False
    if min(deltas) < -3:
        return False
    return True


def evaluate_list(l):
    sublists = [copy.deepcopy(l) for _ in l]
    for j, sublist in enumerate(sublists):
        del sublist[j]
        # print(sublist, end=" ")
        deltas = get_deltas(sublist)
        result = evaluate_deltas(deltas)
        # print(result)
        if result:
            return True
    return False


lists = [[int(x) for x in line.strip().split()] for line in open("input02").readlines()]

# pprint.pprint(lists)
good = 0
for i, l in enumerate(lists):
    result = evaluate_list(l)
    if result:
        good += 1

print(f"total records: {len(lists)}")
print(f"good records: {good}")
