class MessageException(Exception):
    def __init__(self, message: str, *args, **kwargs):
        super(*args, **kwargs).__init__()
        self.message = message
