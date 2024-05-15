def read_file(file_name):
    """
    Read a file and print its content
    """
    print("__CONTENT_START__")

    try:
        with open(file_name, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("__NO_SUCH_FILE__")

    print("__CONTENT_END__")

def main():
    read_file(input())

if __name__ == '__main__':
    main()