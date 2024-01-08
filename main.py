def sum_digits(a):
    if a < 10:
        return a
    else:
        return a % 10 + sum_digits(a // 10)


print(sum_digits(1234))