class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x = len(s)
        l = x // 2
        first_half = s[:l]
        second_half = s[l:]
        c1 = c2 = 0

        vowels = set('aeiouAEIOU')

        for char in first_half:
            if char in vowels:
                c1 += 1

        for char in second_half:
            if char in vowels:
                c2 += 1

        return c1 == c2

# Example usage:
sol = Solution()
result = sol.halvesAreAlike("abcdeABCDE")
print(result)
