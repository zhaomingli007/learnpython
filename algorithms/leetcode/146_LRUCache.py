class CacheNode:
    def __init__(self, pre=None, nxt=None, key=None, val=None):
        self.pre = pre
        self.nxt = nxt
        self.val = val
        self.key = key
        
        
class LRUCache:
    """
    {a:(1, pre, next), b:2,c:3,d:4}
    
     a <-> b <-> c <-> d
     
    ["LRUCache","put","put","get","put","get","put","get","get","get"]
    [[2],        [1,1],[2,2],[1],  [3,3],[2],  [4,4],[1],  [3],  [4]]
    

    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.tail = CacheNode()
        self.head = CacheNode()
        
    
    def _append(self, new_node):
        if self.tail.nxt:
            self.tail.nxt.nxt = new_node
            new_node.pre = self.tail.nxt
        self.tail.nxt = new_node
        if not self.head.nxt:
            self.head.nxt = new_node
            
    
    def _remove(self, to_remove):
        pre = to_remove.pre
        nxt = to_remove.nxt 
        #link up pre and nxt
        if not pre:
            self.head.nxt = nxt
        else:
            pre.nxt = nxt
        if nxt:
            nxt.pre = pre
        if self.tail.nxt == to_remove:
            self.tail.nxt = pre
        #Emptify links
        to_remove.pre , to_remove.nxt = None, None
            
        
    
    def _update(self, to_update):
        self._remove(to_update)
        self._append(to_update)
    
    def get(self, key: int) -> int:
        if key in self.cache:
            k_node = self.cache[key]
            self._update(k_node)
            return k_node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._update(self.cache[key] )
            return 
        cur_cap = len(self.cache)
        if cur_cap >= self.cap:
            #evict 
            to_evict = self.head.nxt
            self.cache.pop(to_evict.key,None)
            self._remove(to_evict)
        new_node = CacheNode(key = key, val = value)            
        self.cache[key] = new_node
        self._append(new_node)
            

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)