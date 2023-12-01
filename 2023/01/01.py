def part_a():
    arr = []
    with open("input", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = "".join(j for j in lines[i] if j.isdigit())
            numb = str(line[0]) + str(line[-1])
            arr.append(int(numb))
    print(sum(arr))

def part_b():
    arr = []
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

    with open("input", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            for k, v in num.items():
                line = line.replace(k, v)
            line = "".join(j for j in line if j.isdigit())
            numb = str(line[0]) + str(line[-1])
            arr.append(int(numb))

    print(sum(arr))


part_a()
part_b()
