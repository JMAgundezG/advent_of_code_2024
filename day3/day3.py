import re

def load_data():
    with open('input.in') as f:
      
        return f.read()

def mul(a):
    return int(a[0]) * int(a[1])

def get_mul_instructions(data):
    return re.findall(r'mul\(\d+\,\d+\)', data)

def get_do_dont_mul_instructions(data):
    return re.findall(r'do\(\)|don\'t\(\)|mul\(\d+\,\d+\)', data)

def solve_day_3_1(data):
    return sum(list(map(lambda x: mul(x[4:-1].split(",")), get_mul_instructions(data))))

def solve_day_3_2(data):
    acc = 0
    action = True
    for i in get_do_dont_mul_instructions(data):
        if i == "do()":
            action = True
        elif i == "don't()":
            action = False
        elif action:
            acc += mul(i[4:-1].split(","))
    return acc

if __name__ == '__main__':
    data = load_data()
    print("DAY 3 EX 1", solve_day_3_1(data))
    print("DAY 3 EX 2", solve_day_3_2(data))