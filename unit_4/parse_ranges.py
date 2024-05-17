def parse_ranges(ranges_string): 
    ranges = ranges_string.split(',')
    s = []
    for r in ranges:
        start, end = r.split('-')
        s += range(int(start), int(end) + 1)
    return (n for n in s)

def main():
    print(list(parse_ranges("1-2,4-4,8-10"))) 
    print(list(parse_ranges("0-0,4-8,20-21,43-45"))) 

if __name__ == '__main__':
    main()