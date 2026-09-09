class LRUCache:

    class ListNode:
        def __init__(self, val=[0,0], next= None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.remspace = capacity
        self.dic = {}
        self.lru = None
        self.mru = None

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.use(node)

            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val[1] = value
            self.use(node)
        else:
            if self.remspace > 0:
                self.remspace -= 1
            else:
                del self.dic[self.lru.val[0]]
                self.lru = self.lru.next
                if self.lru:
                    self.lru.prev = None
            node = self.ListNode([key, value], None, None)
            self.dic[key] = node
            self.use(node)

    def use(self, node: Optional[ListNode]):
        if self.mru == node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
            if self.lru == node:
                self.lru = node.next
        if self.mru:
            node.prev = self.mru
            self.mru.next = node
        if not self.lru:
            self.lru = node
        self.mru = node
        node.next = None
