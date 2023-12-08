input = open("input", "r")
ll = [x for x in input.read().strip().split("\n")]

def part_a():
    ans = []
    for l in ll:
        line = "".join(j for j in l if j.isdigit())
        numb = str(line[0]) + str(line[-1])
        ans.append(int(numb))
    print("Part one:", sum(ans))

def part_b():
    ans = []
    num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3ree",
        "four": "f4or",
        "five": "f5ve",
        "six": "s6x",
        "seven": "s7ven",
        "eight": "e8ght",
        "nine": "n9ne"
    }

    for l in ll:
        for k, v in num.items():
            l = l.replace(k, v)
        line = "".join(j for j in l if j.isdigit())
        numb = str(line[0]) + str(line[-1])
        ans.append(int(numb))

    print("Part two:", sum(ans))

part_a()
part_b()
