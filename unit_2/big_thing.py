class BigThing:
    def __init__(self, size):
        self._size = size
    
    def size(self):
        if isinstance(self._size, int):
            return self._size
        elif isinstance(self._size,(list, str, dict)):
            return len(self._size)

class BigCat(BigThing):
    def __init__(self, size, weight):
        super().__init__(size)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        if self._weight > 15:
            return "Fat"
        
        return "OK" 
        

def main():
    big_thing = BigThing([1, 2, 3])
    print(big_thing.size())
    my_thing = BigThing("balloon")
    print(my_thing.size())
    big_thing = BigThing({1: 'a', 2: 'b'})
    print(big_thing.size())
    big_thing = BigThing(123)
    print(big_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()