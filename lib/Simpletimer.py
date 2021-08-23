import time


class simpletimer:
    def __init__(self):
        self.before = 0

    def millis(self):
        return time.monotonic_ns()/1e6

    def timer(self, time_to_wait=1000):
        if self.millis()-self.before >= time_to_wait:
            self.before = self.millis()
            return True
        else:
            return False
