from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        if not logs:
            return 0
        
        count = 0

        for log in logs:
            if log == './':
                continue
            if log == '../':
                if count == 0:
                    continue
                else:
                    count -= 1
                    continue
            count += 1
        
        return count
            
