def is_funny(string):    
    return all(c == 'h' or c == 'a' for c in string)

def main():
    print(is_funny("lol")) 
    print(is_funny("hhhhaaaahhhh")) 


if __name__ == '__main__':
    main()