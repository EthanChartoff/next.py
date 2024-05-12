def is_prime(number):     
    return all(number % x != 0 for x in range(2, number))

def main():
    print(is_prime(42))
    print(is_prime(43))

if __name__ == '__main__':
    main()