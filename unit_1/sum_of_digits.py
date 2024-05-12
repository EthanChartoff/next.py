def sum_of_digits(number):    
    return sum([int(d) for d in str(number) if d.isdigit()])


def main():
    print(sum_of_digits(104))
    print(sum_of_digits(00000))
    print(sum_of_digits(1991))

if __name__ == '__main__':
    main()