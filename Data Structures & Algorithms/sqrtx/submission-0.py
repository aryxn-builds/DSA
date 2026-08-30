class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            square = m * m

            if square == x:
                return m

            elif square < x:
                res = m
                l = m + 1

            else:
                r = m - 1

        return res