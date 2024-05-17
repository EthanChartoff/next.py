def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'} 
    return ' '.join([words.get(word, word) for word in sentence.split()])

def main():
    print(translate("el gato esta en la casa"))

if __name__ == '__main__':
    main()