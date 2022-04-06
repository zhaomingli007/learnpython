class Solution:
    def myPow(self, x: float, n: int) -> float:
        # print(n)
        if n == 0:
            return 1

        if abs(n) == 1:
            return x if n > 0 else 1/x
        elif abs(n) == 2:
            return x*x if n > 0 else 1/(x*x)

        if n % 2 == 0:
            hf = self.myPow(x, n // 2)
            return hf * hf
        else:
            nn = (n-1) // 2 if n > 0 else (n+1) // 2
            hf = self.myPow(x, nn)
            xx = x if n > 0 else 1/x
            return hf * hf * xx
