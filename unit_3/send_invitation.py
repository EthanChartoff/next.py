class UnderAgeException(Exception):
    def __init__(self, age):
        super().__init__()
        self.age = age

    def __str__(self):
        return f"under age come back in {18 - self.age} years"


def send_invitation(name, age):
    try:
        if age < 18:
            raise UnderAgeException(age)
        print("You should send an invite to " + name)
    except UnderAgeException as e:
        print(e)
            

def main():
    send_invitation("g", int(input()))

if __name__ == '__main__':
    main()