def double_letter(my_str):    
    return ''.join([letter * 2 for letter in my_str])


def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))


if __name__ == '__main__':
    main()