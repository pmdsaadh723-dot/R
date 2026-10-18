class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7        
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            ways_to_interleave = nCr(len(left) + len(right), len(left))
            return (ways_to_interleave * dfs(left) * dfs(right)) % MOD
        return (dfs(nums) - 1) % MOD