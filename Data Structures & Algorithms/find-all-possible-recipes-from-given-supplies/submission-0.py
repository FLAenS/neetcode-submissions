from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        rec = deque(range(len(recipes)))
        sup = set(supplies)
        fails = 0
        res = []
        while rec and fails < len(rec):
            cur = rec.popleft()
            if all(ing in sup for ing in ingredients[cur]):
                res.append(recipes[cur])
                sup.add(recipes[cur])
                fails = 0
            else:
                rec.append(cur)
                fails += 1
        return res 
