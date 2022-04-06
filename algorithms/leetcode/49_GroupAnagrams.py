from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["eat","tea","tan","ate","nat","bat"]
        {1:{e:1,a:1, t:1}, 2:{t:1}}
        """
        adj = defaultdict(list)

        for s in strs:
            adj[tuple(sorted(s))].append(s)

        return adj.values()
