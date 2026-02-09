class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_cap = 0
        self.cache = dict()
        self.leftb = Node(-1,-1)
        self.rightb = Node(-1,-1)
        self.leftb.next, self.rightb.prev = self.rightb, self.leftb

    def delete_node(self, node):
        self.cache.pop(node.key)
        node.next.prev, node.prev.next = node.prev, node.next
        self.curr_cap -= 1
    
    def insert_node_at_beginning(self, key, val):
        node = Node(key, val, self.leftb, self.leftb.next)
        self.leftb.next = node
        node.next.prev = node
        self.cache[key] = node
        self.curr_cap += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            self.delete_node(node)
            self.insert_node_at_beginning(key, value)
        else:
            value = -1

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete_node(self.cache[key])
        elif self.curr_cap >= self.capacity:
            self.delete_node(self.rightb.prev)
        
        self.insert_node_at_beginning(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)