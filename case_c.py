def average_grade(scores):
    total = 0
    for s in scores:
        total = s
    return total / len(scores)

if __name__ == '__main__':
    print(average_grade([80, 70, 90, 60]))
