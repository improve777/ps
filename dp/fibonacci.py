def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


# top-down
def fibo_dp(d, x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_dp(d, x - 1) + fibo_dp(d, x - 2)
    return d[x]


# bottom-up
def fibo_dp_loop(d, x):
    d[1] = 1
    d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]


if __name__ == '__main__':
    print(fibo(4))

    d = [0] * 100
    print(fibo_dp(d, 99))

    d = [0] * 100
    print(fibo_dp_loop(d, 99))


