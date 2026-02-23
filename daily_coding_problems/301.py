import hashlib

class BloomFilter:
    """
    Implement a data structure which carries out the following operations without resizing the underlying array:

    add(value): Add a value to the set of values.
    check(value): Check whether a value is in the set.
    The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set), but should always correctly identify a true element.
    """

    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [0] * size

    def _hashes(self, value):
        value = str(value).encode()
        for i in range(self.num_hashes):
            h = hashlib.sha256(value + bytes([i])).hexdigest()
            yield int(h, 16) % self.size

    def add(self, value):
        for idx in self._hashes(value):
            self.bits[idx] = 1

    def check(self, value):
        for idx in self._hashes(value):
            if self.bits[idx] == 0:
                return False
        return True
