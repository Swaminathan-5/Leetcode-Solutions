class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        curgas = 0
        for i in range(len(gas)):
            curgas += gas[i] - cost[i]
            if curgas < 0:
                start = i + 1
                curgas = 0
        return start