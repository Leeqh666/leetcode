class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n == 0 or n == 2:
            return 0
        self.res = set()
        relation = {}
        for pair in pairs:
            relation[pair[0]] = pair[1]
            relation[pair[1]] = pair[0]
        
        members = [i for i in range(n)]
        for i in members:
            if i in self.res:
                continue
            preferences_i = preferences[i][0: preferences[i].index(relation[i])]
            for preference in preferences_i:
                if preferences[preference].index(i) < preferences[preference].index(relation[preference]):
                    self.res.add(i)
                    self.res.add(preference)
        return len(self.res)

