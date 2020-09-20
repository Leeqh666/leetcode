class Solution:
    def modifyString(self, s: str) -> str:
        my_list = [c for c in s]
        if len(my_list) == 1:
            if my_list[0] == '?':
                my_list[0] = self.select([])
            return ''.join(my_list)
            
        indexes = []
        for i, c in enumerate(my_list):
            if c == '?':
                indexes.append(i)
        
        for index in indexes:
            c = []
            if index == 0:
                c.append(my_list[index + 1])
            elif index == len(my_list) - 1:
                c.append(my_list[index - 1])
            else:
                c.append(my_list[index - 1])
                c.append(my_list[index + 1])
            
            my_list[index] = self.select(c)
        
        return ''.join(my_list)
            
        
    def select(self, c):
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(26):
            if characters[i] not in c:
                return characters[i]




            