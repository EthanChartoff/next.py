class MusicNotes:
    FREQS = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
    MAX_OCTAVE = 4

    def __init__(self):
        self.i = 0
        self.octave = 0 

    def __iter__(self):
        self.i = 0
        self.octave = 0
        return self

    def __next__(self):
        if self.i >= len(self.FREQS):
            self.i = 0
            self.octave += 1
            if self.octave > self.MAX_OCTAVE:
                raise StopIteration

        freq = self.FREQS[self.i]
        self.i += 1
        return freq * (2 ** self.octave)

def main():
    notes_iter = iter(MusicNotes())

    for freq in notes_iter:
        print(freq)

if __name__ == '__main__':
    main()