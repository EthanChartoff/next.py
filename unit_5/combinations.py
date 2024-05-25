from itertools import combinations

def combi():
    wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    for i in range(0, len(wallet)):
        for money in combinations(wallet, i):
            if sum(money) == 100:
                yield money

def main():
    print(len(set(combi())))

if __name__ == '__main__':
    main()