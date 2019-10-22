from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        size = len(candidates)
        self.trace(0, candidates, res, path, target, size)
        return res

    def trace(self, begin, candidates, res, path, target, size):
        if target == 0:
            res.append(path[:])
        for i in range(begin, size):
            residual = target - candidates[i]
            if residual < 0:
                break
            path.append(candidates[i])
            self.trace(i+1, candidates, res, path, residual, size)
            path.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    print(result)