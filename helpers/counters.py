class Counter:

    def __init__(

        self,

        start

    ):

        self.value = start

    def next(self):

        current = self.value

        self.value += 1

        return current
