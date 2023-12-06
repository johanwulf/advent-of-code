input = open("input", "r")
ll = [x for x in input.read().strip().split("\n")]

def part_one():
    ans = 1
    time = [eval(i) for i in ll[0].split(":")[1].split()]
    dist = [eval(i) for i in ll[1].split(":")[1].split()]

    for i in range(len(time)):
        wins = 0
        for speed in range(time[i]):
            travel = (time[i] - speed) * speed 
            if travel > dist[i]:
                wins += 1
            ans *= wins

    print("one", ans)

def part_two():
    ans = 1
    time = [int(ll[0].split(":")[1].replace(" ", ""))]
    dist = [int(ll[1].split(":")[1].replace(" ", ""))]

    for i in range(len(time)):
        wins = 0
        for speed in range(time[i]):
            travel = (time[i] - speed) * speed 
            if travel > dist[i]:
                wins += 1
            ans *= wins

    print("one", ans)

part_one()
part_two()
