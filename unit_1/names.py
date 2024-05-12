from functools import reduce 

def get_longest_name():    
    return max((line.strip() for line in open("/home/goodman/school/next.py/unit_1/names.txt")), key=len, default='')

def sum_names():
    return sum((len(line.strip()) for line in open("/home/goodman/school/next.py/unit_1/names.txt")))

def get_shortest_names():
    return '\n'.join(list(filter(lambda x: len(x) == min((len(name.strip()) for name in open("/home/goodman/school/next.py/unit_1/names.txt")), default=0), (line.strip() for line in open("/home/goodman/school/next.py/unit_1/names.txt")))))

def write_names_len():
    open("/home/goodman/school/next.py/unit_1/name_length.txt", "w").write('\n'.join(list((str(len(line.strip())) for line in open("/home/goodman/school/next.py/unit_1/names.txt")))))

def get_names_of_length():
    length = int(input("Enter name length: "))
    return '\n'.join(list(filter(lambda x: len(x) == length, (line.strip() for line in open("/home/goodman/school/next.py/unit_1/names.txt")))))

def main():
    print(get_names_of_length())

if __name__ == '__main__':
    main()