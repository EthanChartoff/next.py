class GreetingCard:
    def __init__(self, recipient = "Dana Ev", sender = "Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        return f"Hello {self._recipient} from {self._sender}"