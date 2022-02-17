class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for a in operations:
            if a.find('+')>=0: x+=1
            elif a.find('-')>=0: x-=1
        return x