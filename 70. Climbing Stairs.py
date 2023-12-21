class Solution:
    def climbStairs(self, n: int) -> int:
        temp = {}
        return self.fibonacci(n, temp)

    def fibonacci(self, n, temp):
        if n == 0 or n == 1:
            return 1

        elif n not in temp:
            temp[n] = self.fibonacci(n - 1, temp) + self.fibonacci(n - 2, temp)

        return temp[n]
