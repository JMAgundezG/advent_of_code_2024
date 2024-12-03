def load_data():
    with open('input.in') as f:
        data = []
        for line in f:
            data.append(list(map(int, line.strip().split())))
    return data

def report_safe(report):
    """
    Given a list there is no difference bigger than 2 between the nearest elements
    """
    for i in range(1, len(report)):
        delta = abs(report[i] - report[i - 1])
        if delta not in range(1, 4):
            return False
 
    return sorted(report) in [report, report[::-1]]

def report_almost_safe(report):
    return report_safe(report) or any([report_safe(report[:i] + report[i + 1:]) for i in range(len(report))])

def solve_day_2_1(data):
    
    return list(map(report_safe, data)).count(True)


def solve_day_2_2(data):
    return list(map(report_almost_safe, data)).count(True)

if __name__ == '__main__':
    data = load_data()
    # data = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 2, 1], [1,3,6,7,9]]
    print("DAY 2 EX 1", solve_day_2_1(data))
    print("DAY 2 EX 2", solve_day_2_2(data))