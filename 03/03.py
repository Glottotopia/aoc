import re


MUL = re.compile("mul\(([0-9]+),([0-9]+)\)")
def get_sum(s):
    muls = MUL.findall(s)
    # print(muls)
    results = [int(mul[0])*int(mul[1]) for mul in muls]
    # print(results)
    total = sum(results)
    print(f"The sum of all multiplications is {total}")

with open("input") as in_:
    s = in_.read()
    get_sum(s)
    do_s = s.split("do()")
    do_s_no_don_t_s = ''.join([do.split("don't()")[0] for do in do_s])
    get_sum(do_s_no_don_t_s)



