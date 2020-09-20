class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0
        for c in text:
            if c == ' ':
                count += 1
        
        if count == 0:
            return text
        
        texts = text.split()
        n = len(texts)
        if n == 1:
            return texts[0] + ' ' * count
        b = count // (n - 1)
        extra = ' ' * b
        extra = extra.join(texts)
        if count % (n - 1) == 0:
            return extra
        else:
            extra += ' ' * (count % (n - 1))
        
        return extra

