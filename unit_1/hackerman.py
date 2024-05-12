def hackerman(s):     
    return ''.join([chr(ord(c) + 2) if c.isalpha() else c for c in s])


def main():
    print(hackerman("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))


if __name__ == '__main__':
    main()