input = open("input", "r")
ll = [x for x in input.read().strip().split("\n")]

def part_a():
    ret = []
    for l in ll:
        game_number = l.split()[1].strip(":")
        game = l.split(":")[1].strip().split(";")
        flag = True 
    
        for g in game:
            cubes = {"red": 12, "green": 13, "blue": 14}
            subset = g.strip().split(",")
            for i in range(len(subset)):
                val, color = subset[i].strip().split(" ")
                cubes[color] -= int(val)

            for _, value in cubes.items():
                if value < 0:
                    flag = False
                    break

        if flag:
            ret.append(int(game_number))

    print(ret)
    print("Part one", sum(ret))

def part_b():
    ret = 0
    for l in ll:
        game = l.split(":")[1].strip().split(";")
        cubes = {"red": 0, "green": 0, "blue": 0}
        for g in game:
            subset = g.strip().split(",")
            for s in subset: 
                val, color = s.strip().split(" ")
                cubes[color] = max(cubes[color], int(val))

        ret += cubes["red"] * cubes["green"] * cubes["blue"]
    print("Part two", ret)

part_a()
part_b()
