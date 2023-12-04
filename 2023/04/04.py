from collections import defaultdict

input = open("input", "r")
ll = [x for x in input.read().strip().split("\n")]

def part_one():
    ans = 0
    for l in ll:
        win = l.split(":")[1].split("|")[0].strip().split()
        nums = l.split(":")[1].split("|")[1].strip().split()
        no_win = len([x for x in win if x in nums])
        tot = 0

        if no_win > 0:
            tot += 2**(no_win-1)

        ans += tot 

    print("Part one: ", ans)

def part_two():
    ans = defaultdict(int)
    for i, l in enumerate(ll):
        ans[i] += 1
        win = l.split(":")[1].split("|")[0].strip().split()
        nums = l.split(":")[1].split("|")[1].strip().split()
        no_win = len([x for x in win if x in nums])

        for j in range(no_win):
            ans[i+1+j] += ans[i]

    print("Part two:", sum(ans.values()))

part_one()
part_two()
