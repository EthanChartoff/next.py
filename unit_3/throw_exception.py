def raiseStopIteration():
    raise StopIteration

def raiseZeroDivisionError():
    raise ZeroDivisionError

def raiseAssertionError():
    raise AssertionError

def reaiseImportError():
    raise ImportError

def raiseKeyError():
    raise KeyError

def raiseSyntaxError():
    raise SyntaxError

def raiseIndentationError():
    raise IndentationError

def raiseTypeError():
    raise TypeError

def main():
    functions = [
        raiseStopIteration, 
        raiseZeroDivisionError, 
        raiseAssertionError,
        reaiseImportError, 
        raiseKeyError, 
        raiseSyntaxError,
        raiseIndentationError, 
        raiseTypeError
    ]

    for f in functions:
        try:
            f()
        except Exception as e:
            print(type(e). __name__)

if __name__ == '__main__':
    main()

