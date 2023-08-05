class NotTypeHintException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Not type hint in function: {}".format(self.message)
