class Sender(object):
    def __init__(self, channel_id, protocol):
        self.channel_id = channel_id
        self.protocol = protocol

    def send_method(self, method):
        self.protocol.send_method(self.channel_id, method)


class Actor(object):
    def __init__(self, synchroniser, sender):
        self.synchroniser = synchroniser
        self.sender = sender

    def handle(self, frame):
        try:
            meth = getattr(self, 'handle_' + type(frame).__name__)
        except AttributeError:
            meth = getattr(self, 'handle_' + type(frame.payload).__name__)

        meth(frame)

    def handle_PoisonPillFrame(self, frame):
        self.synchroniser.killall(ConnectionError)
