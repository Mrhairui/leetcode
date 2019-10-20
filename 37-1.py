from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        candidates.sort()
        if size == 0:
            return []
        path = []
        res = []
        self.demo(candidates, 0, size, path, res, target)
        return res
    def demo(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])

        for i in range(begin, size):
            residual = target - candidates[i]
            if residual < 0:
                break
            path.append(candidates[i])
            self.demo(candidates, i, size, path, res, residual)
            path.pop()



if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
