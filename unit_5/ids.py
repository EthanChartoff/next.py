class IDIterator:
    MIN_ID = 0
    MAX_ID = 999999999

    def __init__(self, id = 0):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        while self._id <= IDIterator.MAX_ID:
            self._id += 1
            if check_id_valid(self._id):
                return self._id
            
        raise StopIteration

def check_id_valid(id_number):
    return sum(list(map(lambda x: x if x < 10 else x - 9, map(lambda x, i: int(x) if i % 2 == 0 else int(x) * 2, str(id_number), range(len(str(id_number))))))) % 10 == 0

def id_generator(id = 0):
    while id <= IDIterator.MAX_ID:
        id += 1
        if check_id_valid(id):
            yield id

    raise StopIteration

def main():
    id = int(input("enter ID: "))
    c = input("Generator or Iterator? (gen/it)? ")

    it = iter(IDIterator(id))
    gen = id_generator(id)

    if c == "gen":
        for _ in range(10):
            print(next(gen))

    if c == "it":
        for _ in range(10):
            print(next(it))

if __name__ == '__main__':
    main()