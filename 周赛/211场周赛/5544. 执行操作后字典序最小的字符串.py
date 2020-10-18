class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        b %= n
        ss = set()
        res = "1" + '0' * 101   # 最多是1e100

        def backtrace(ts):
            nonlocal res, ss

            if int(res) > int(ts):
                res = ts
            if ts in ss:  # 如果一个情况之前遇到过，说明可以终结循环了  暂时没想到减枝的方法
                return
            ss.add(ts)

            backtrace(ts[b:]+ts[:b])  # 1.先搜索旋转的情况

            ts = list(ts)
            for i in range(1, n, 2):   # 为所有奇位加上a
                ts[i] = str((int(ts[i]) + a) % 10)
            ts = ''.join(ts)

            backtrace(ts)  # 2.然后遍历奇位加上a的情况

        backtrace(s)
        return res