from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n = len(prerequisites)

        #1. init adjacent list {1:[0,2], 2:[1]}
        adj_list = defaultdict(list)
        for p, q in prerequisites:
            adj_list[q].append(p)

        # print(adj_list)

        #2. check circles using dfs
        has_circle = False
        v = set()  # mark visited node

        def dfs(node, p_set):
            """
            :p_set check if there is a circle in the graph
            """
            nonlocal has_circle
            # print(node, p_set)
            if has_circle or node in p_set:
                has_circle = True
                return
            p_set.add(node)
            for adj_n in adj_list[node]:
                if adj_n not in v:
                    dfs(adj_n, p_set)
                    if adj_n in p_set:
                        p_set.remove(adj_n)
            v.add(node)

        for k in list(adj_list):
            if has_circle:
                break
            # print('start',k)
            if k not in v:
                dfs(k, set())

        return not has_circle
