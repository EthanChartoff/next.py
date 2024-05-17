def is_prime(n):    
    return not any(n % i == 0 for i in range(2,n))

def first_prime_over(n):
    return next(i for i in range(n+1, 2*n) if is_prime(i))

def main():
    print(first_prime_over(1000000))    

if __name__ == '__main__':
    main()