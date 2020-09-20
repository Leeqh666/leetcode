import collections
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        s1 = [int(c) for c in s]
        t1 = [int(c) for c in t]
        if collections.Counter(s1)!=collections.Counter(t1): return False
        idx = collections.defaultdict(list)
        for i,v in enumerate(s1):
            heads = sum([len(idx[k]) for k in range(v+1)])
            idx[v].append(heads)
        for i,v in enumerate(t1):
            if i<idx[v][0]: return False
            idx[v].pop(0)
        return True