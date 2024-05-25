from file1 import GreetingCard
from file2 import BirthdayCard

def main():
    print(GreetingCard().greeting_msg())
    print(BirthdayCard(21).greeting_msg())

if __name__ == "__main__":
    main()