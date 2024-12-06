    
def load_data():
    rules = []
    pages = []

    with open('input.in') as f:
        for line in f:
            if "|" in line:
                rules.append(line)
            else:
                if line.strip():
                    pages.append(line)
    
    clean_rules = {}
    for rule in rules:
        before, after = rule.strip().split("|")
        if int(before) not in clean_rules:
            clean_rules[int(before)] = [int(after)]
        else:
            clean_rules[int(before)].append(int(after))
    
    clean_pages = [[int(i) for i in page.strip().split(',') if page.strip()] for page in pages]
    return clean_rules, clean_pages

def verify_update(rules, update, fix):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            ruled_numbers = rules.get(update[j], [])
            if update[i] in ruled_numbers:
                if not fix:
                    return 0
                else:
                    up2 = update.copy()
                    up2[i], up2[j] = up2[j], up2[i]
                    return verify_update(rules, up2, True)
    
    return int(update[len(update) // 2])

def solve_day_5_1(rules, pages):
    return sum(map(lambda x: verify_update(rules, x, False), pages))



def solve_day_5_2(rules, pages):
    return sum(map(lambda x: verify_update(rules, x, True), pages)) - solve_day_5_1(rules, pages)

if __name__ == '__main__':
    rules, pages = load_data()

    print("DAY 5 EX 1", solve_day_5_1(rules, pages))
    print("DAY 5 EX 2", solve_day_5_2(rules, pages))
