def recursive_nth_fibo(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        soucet = recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)
        return soucet


def main(n):
    return recursive_nth_fibo(n)


if __name__ == "__main__":
    main(7)
