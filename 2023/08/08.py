from collections import defaultdict
import math

input = open("input", "r")
ll = [x for x in input.read().strip().split("\n\n")]

def part_one():
    rl = list(ll[0]*100000)
    map = ll[1:][0].split("\n")

    d = {}
    for inst in map: 
        s = inst.split(" ")[0].strip()
        r, l = inst.split("(")[1].split(")")[0].strip().split(",")
        r = r.strip()
        l = l.strip()
        d[s] = (r, l)

    curr = "AAA"
    count = 0;

    while curr != "ZZZ":
        inst = rl[count]
        if inst == "R":
            curr = d[curr][1]
        elif inst == "L":
            curr = d[curr][0]
        count += 1

    print("one", count)

def part_two():
    rl = list(ll[0]*100000)
    map = ll[1:][0].split("\n")

    d = {}
    for inst in map: 
        s = inst.split(" ")[0].strip()
        r, l = inst.split("(")[1].split(")")[0].strip().split(",")
        r = r.strip()
        l = l.strip()
        d[s] = (r, l)

    curr = [k for k,_ in d.items() if k[2] == "A"]
    res = []
    
    for c in curr:
        count = 0
        while c[2] != "Z":
            inst = rl[count]
            if inst == "R":
                c = d[c][1]
            elif inst == "L":
                c = d[c][0]
            count += 1
        res.append(count)

    print("two", math.lcm(*res))

part_one()
part_two()
