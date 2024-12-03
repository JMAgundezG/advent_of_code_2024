def load_data():
    with open('input.in') as f:
        data = []
        for line in f:
            data.append(list(map(int, line.strip().split())))
    return data

    

def solve_day_1(data):
    first = list(map(lambda x: x[0], data))
    second = list(map(lambda x: x[1], data))
    first.sort()
    second.sort()
    
    acc = 0
    print(first, second)

    for i in range(len(first)):
        acc += abs(first[i] - second[i])

    return acc

def solve_day_2(data):
    first = list(map(lambda x: x[0], data))
    second = list(map(lambda x: x[1], data))
    silly_cache_for_silly_things = {}
    acc = 0

    for i in first:
        if i not in silly_cache_for_silly_things:
            silly_cache_for_silly_things[i] = second.count(i) * i
        acc += silly_cache_for_silly_things[i]

    return acc
if __name__ == '__main__':
    data = load_data()
    # data = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]] # load_data()
    print("DAY 1 EX 1", solve_day_1(data))
    print("DAY 1 EX 2", solve_day_2(data))
