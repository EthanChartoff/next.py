def gen_secs():
    for i in range(60):
        yield i

def gen_minutes():
    for i in range(60):
        yield i

def gen_hours():
    for i in range(24):
        yield i

def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield f'{h:02d}:{m:02d}:{s:02d}'    

def gen_years(start=2024):
    while True:
        yield start
        start += 1

def gen_months():
    for i in range(1, 13):
        yield i

def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2 and leap_year:
        max_days = 29
    else:
        max_days = 28
    for i in range(1, max_days + 1):
        yield i

def gen_dates():
    for y in gen_years():
        for m in gen_months():
            for d in gen_days(m, y % 4 == 0):
                for h in gen_hours():
                    for mi in gen_minutes():
                        for s in gen_secs():
                            yield f'{d:02d}/{m:02d}/{y:04d} {h:02d}:{mi:02d}:{s:02d}'
                

def main():
    i = 0
    for d in gen_dates():
        if i % 10 ** 6 == 0:
            print(d)
        i += 1

if __name__ == '__main__':
    main()