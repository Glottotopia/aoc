lists = [[int(x) for x in line.strip().split()] for line in open("input").readlines()]

list1 = [x[0] for x in lists]
list2 = [x[1] for x in lists]

list1.sort()
list2.sort()

joint_list = zip(list1, list2)

result = 0
print(f"There are {len(lists)} records")
for x in joint_list:
    delta = abs(x[0] - x[1])
    result += delta
print(f"The distance is {result}")

similarity_list = []
for x in list1:
    occurrences = list2.count(x)
    score = x * occurrences
    similarity_list.append(score)
similarity_total = sum(similarity_list)
print(f"The total similarity score is {similarity_total}")
