class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinChanges = [float('inf')] * (amount + 1)
        coinChanges[0] = 0

        for i in range(1, amount + 1):
            if i in coins:
                coinChanges[i] = 1
            else:
                for coin in coins:
                    if i >= coin:
                        coinChanges[i] = min(coinChanges[i], coinChanges[i - coin] + 1)
        if coinChanges[-1] == float('inf'):
            return -1
        else:
            return coinChanges[-1]