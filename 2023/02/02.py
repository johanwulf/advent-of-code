import re

input = open("input", "r")

ll = [x for x in input.read().strip().split("\n")]

def part_a():
    ret = 0
    flag = True
    for l in ll:
        game = l.split(" ")[1].strip(":")
        subset = l.split(":")[1].strip().split(";")
        flag = True 
    
        for i in range(len(subset)):
            red = 12
            green = 13
            blue = 14
            nam = subset[i].split(",")
            for i in range(len(nam)):
                val = re.search(r'\d+', nam[i])
                sum = 0
                if val:
                    sum = int(val.group())
                if "red" in nam[i]:
                    red -= sum 
                elif "green" in nam[i]:
                    green -= sum 
                elif "blue" in nam[i]:
                    blue -= sum
            if red < 0 or green < 0 or blue < 0:
                flag = False

        if flag:
            ret += int(game) 
    print(ret)

def part_b():
    ret = 0
    for l in ll:
        subset = l.split(":")[1].strip().split(";")
        red = 0
        green = 0
        blue = 0 
        for i in range(len(subset)):
            nam = subset[i].split(",")
            for i in range(len(nam)):
                val = re.search(r'\d+', nam[i])
                sum = 0
                if val:
                    sum = int(val.group())
                if "red" in nam[i] and sum > red:
                    red = sum
                elif "green" in nam[i] and sum > green:
                    green = sum
                elif "blue" in nam[i] and sum > blue:
                    blue = sum
        ret += red * blue * green
    print(ret)

part_a()
part_b()
