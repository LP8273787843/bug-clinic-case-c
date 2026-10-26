def average_grade(scores):
    # FIX 2: guard against an empty list (original crashed with ZeroDivisionError)
    if len(scores) == 0:
        raise ValueError('scores must not be empty')
    total = 0
    for s in scores:
        total = total + s  # FIX 1: accumulate each score (was 'total = s', which overwrote it)
    return total / len(scores)

if __name__ == '__main__':
    print(average_grade([80, 70, 90, 60]))
