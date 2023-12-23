class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hp = []
        for i in arr:
            heapq.heappush(hp, (abs(i - x), i))

        ans = []
        while k:
            temp = heapq.heappop(hp)
            ans.append(temp[1])
            k -= 1

        ans.sort()
        return ans
