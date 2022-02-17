

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use a stack and do dfs
        4
        [[1,0],[2,0],[3,1]]
        Adj list
        0->[1,2]
        1->[3]
        2->[]
        3->[]

        [[2,0],[1,0],[3,1],[3,2],[1,3]]
        0: [1,2]
        1: [3]
        2: [3]
        3: [1]
        """
        adj_list = defaultdict(list)
        for p, q in prerequisites:
            adj_list[q].append(p)

        # print(adj_list)
        s = deque()
        v = set()
        has_cir = False

        def dfs(node, pth_set=set()):
            """
            :type path: set to check circle
            """
            nonlocal has_cir
            #check neighbours
            nbs = adj_list[node]
            # print(node)
            pth_set.add(node)
            for nb in nbs:
                if nb in pth_set:
                    # print(pth_set, nb)
                    # print('circle')
                    has_cir = True
                    return
                if nb not in v:
                    dfs(nb, pth_set)
            pth_set.remove(node)
            if node not in v:
                # print('append', node)
                s.appendleft(node)
                v.add(node)

        for k in list(adj_list):
            if not has_cir:
                dfs(k)
        # print(has_cir)

        for c in range(numCourses):
            if c not in v:
                v.add(c)
                s.appendleft(c)

        return s if not has_cir else []
