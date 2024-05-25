def triple_step():
    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i) 

def main():
    triple_step()

if __name__ == '__main__':
    main()