class Node:
    def __init__(self, k, v):
        self.key, self.value = k, v
        self.prev, self.nxt = None, None

class LRUCache:
    def __init__(self, capacity: int):
        # key: key. value: node.
        self.cache = {}
        # header nodes for left and right
        self.left, self.right = Node(0, 0), Node(0, 0)
        # point them at each other
        self.left.nxt = self.right
        self.right.prev = self.left
        self.capacity = capacity 

    def insert(self, node):
        # insert before right (because its now the most frequently used)
        r = self.right
        l = self.right.prev
        l.nxt = node
        r.prev = node
        node.nxt = r
        node.prev = l
    
    def remove(self, node):
        p = node.prev        
        n = node.nxt
        p.nxt = n
        n.prev = p

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new = Node(key, value)
        self.insert(new)
        self.cache[key] = new
        
        if len(self.cache) > self.capacity:
            # evict LRU
            lru = self.left.nxt
            self.cache.pop(lru.key)
            self.remove(lru)










