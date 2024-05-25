from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, sender_age = 0):
        super().__init__()
        self._sender_age = sender_age

    def greeting_msg(self):
        return f"Happy Birthday {self._recipient} from {self._sender} who is {self._sender_age} years old"

