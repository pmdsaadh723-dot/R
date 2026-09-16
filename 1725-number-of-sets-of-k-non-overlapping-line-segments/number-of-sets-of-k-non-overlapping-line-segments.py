class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1000000007
        total = n + k - 1
        r = 2 * k
        fact = [1] * (total + 1)
        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i % MOD
        numerator = fact[total]
        denominator = fact[r] * fact[total - r] % MOD
        answer = numerator * pow(denominator, MOD - 2, MOD) % MOD
        return answer  