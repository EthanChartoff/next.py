def combine_coins(coin, numbers):
    return ', '.join([coin + str(n) for n in numbers])


def main():
    print(combine_coins('$', range(5)))


if __name__ == '__main__':
    main()