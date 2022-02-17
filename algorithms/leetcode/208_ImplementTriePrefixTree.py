class TrieNode:
    def __init__(self, word_end):
        self.links = {}
        self.word_end = word_end


class Trie:
    """
    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
            a
           / \
          l   p
         / \   \
        i   a   p
       / \   \   \
      b   l   a   l
                   \
                    e
    a->p->p->l->e
     ->l->a->a
        ->i->l
           ->b
    a, p, p, 
    
    1
     
    []
    """

    def __init__(self):
        self.root = TrieNode(True)

    def insert(self, word: str) -> None:
        nxt_nd = self.root
        for c in word:
            #get next node and insert
            if c not in nxt_nd.links:
                nxt_nd.links[c] = TrieNode(False)
            #create c with new trie node
            nxt_nd = nxt_nd.links[c]
        nxt_nd.word_end = True

    def _is_end(self, node, c):
        return node.links[c].word_end

    def search(self, word: str) -> bool:
        nd = self.root
        n = len(word)
        print(word)
        for i, c in enumerate(word):
            if c in nd.links:
                # print(c, self._is_end(nd,c), list(nd.links))
                if self._is_end(nd, c) and i == n-1:
                    return True
                nd = nd.links[c]
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        nd = self.root
        for i, c in enumerate(prefix):
            if c in nd.links:
                if i == n-1:
                    return True
                nd = nd.links[c]
            else:
                return False
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
