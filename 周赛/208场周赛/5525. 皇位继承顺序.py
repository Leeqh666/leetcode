from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.father_son = defaultdict(list)
        self.death_set = set()
        self.curOrder = list()
        self.curOrder.append(self.king_name)

    def birth(self, parentName: str, childName: str) -> None:
        self.father_son[parentName].append(childName)

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:

        def successor(x, order):
            for son in self.father_son[x]:
                self.curOrder.append(son)
                successor(son, self.curOrder)
                    
        self.curOrder = [self.king_name]
        successor(self.king_name, self.curOrder)
        
        res = []
        for human in self.curOrder:
            if human in self.death_set:
                continue
            else:
                res.append(human)
        return res
        






# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()