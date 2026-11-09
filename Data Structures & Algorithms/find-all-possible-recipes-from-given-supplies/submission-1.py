from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = {}
        for i, r in enumerate(recipes):
            indeg[r] = len(ingredients[i])
            for ind in ingredients[i]:
                graph[ind].append(r)

        q = deque(supplies)
        res = []
        while q:
            sup = q.popleft()
            for r in graph[sup]:
                indeg[r] -= 1
                if indeg[r] == 0:
                    res.append(r)
                    q.append(r)
        return res
