import re
def load_data():
    with open('input.in') as f:
        return f.readlines()

def find_xmas(data):
    s_data = [[i for i in j] for j in data]
    acc = 0
    for i in range(len(s_data)):
        for j in range(len(s_data[i])):
            if j < len(s_data) - 3: # HORIZONTAL
                if s_data[i][j] == 'X' and s_data[i][j + 1] == 'M' and s_data[i][j + 2] == 'A' and s_data[i][j + 3] == 'S':
                    acc += 1
                if s_data[i][j] == 'S' and s_data[i][j + 1] == 'A' and s_data[i][j + 2] == 'M' and s_data[i][j + 3] == 'X':
                    acc += 1
            if i < len(s_data[i]) - 4: # VERTICAL
                if s_data[i][j] == 'X' and s_data[i + 1][j] == 'M' and s_data[i + 2][j] == 'A' and s_data[i + 3][j] == 'S':
                    acc += 1
                if s_data[i][j] == 'S' and s_data[i + 1][j] == 'A' and s_data[i + 2][j] == 'M' and s_data[i + 3][j] == 'X':
                    acc += 1
    
            if i < len(s_data) - 3 and j < len(s_data[i]) - 3: # DIAGONAL
                if s_data[i][j] == 'X' and s_data[i + 1][j + 1] == 'M' and s_data[i + 2][j + 2] == 'A' and s_data[i + 3][j + 3] == 'S':
                    acc += 1
                if s_data[i][j] == 'S' and s_data[i + 1][j + 1] == 'A' and s_data[i + 2][j + 2] == 'M' and s_data[i + 3][j + 3] == 'X':
                    acc += 1
            if i < len(s_data) - 3 and j > 2: # DIAGONAL
                if s_data[i][j] == 'X' and s_data[i + 1][j - 1] == 'M' and s_data[i + 2][j - 2] == 'A' and s_data[i + 3][j - 3] == 'S':
                    acc += 1
                if s_data[i][j] == 'S' and s_data[i + 1][j - 1] == 'A' and s_data[i + 2][j - 2] == 'M' and s_data[i + 3][j - 3] == 'X':
                    acc += 1
                
    return acc

def find_x_mas(data):

    s_data = [[i for i in j] for j in data]
    acc = 0
    for i in range(1, len(s_data) - 1):
        for j in range(1, len(s_data[i]) - 1):
            if s_data[i][j] == 'A':
                if s_data[i - 1][j - 1] == 'M' and s_data[i + 1][j - 1] == 'M' and s_data[i + 1][j + 1] == 'S' and s_data[i - 1][j + 1] == 'S':
                    acc += 1
                if s_data[i - 1][j - 1] == 'M' and s_data[i + 1][j - 1] == 'S' and s_data[i + 1][j + 1] == 'S' and s_data[i - 1][j + 1] == 'M':
                    acc += 1
                if s_data[i - 1][j - 1] == 'S' and s_data[i + 1][j - 1] == 'M' and s_data[i + 1][j + 1] == 'M' and s_data[i - 1][j + 1] == 'S':
                    acc += 1
                if s_data[i - 1][j - 1] == 'S' and s_data[i + 1][j - 1] == 'S' and s_data[i + 1][j + 1] == 'M' and s_data[i - 1][j + 1] == 'M':
                    acc += 1

    return acc

def solve_day_4_1(data):
    return find_xmas(data)


def solve_day_4_2(data):
    return find_x_mas(data)

if __name__ == '__main__':
    data = load_data()

    print("DAY 4 EX 1", solve_day_4_1(data))
    print("DAY 4 EX 2", solve_day_4_2(data))