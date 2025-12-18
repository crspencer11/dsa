class MyHashSet:

    def __init__(self):
       self.HashSet = [] 

    def add(self, key: int) -> None:
        self.HashSet.append(key)

    def remove(self, key: int) -> None:
        while self.contains(key):
            self.HashSet.remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.HashSet:
            return True
        return False
