class Solution:
    def search(self, nums, target: int) -> int:

            n = len(nums)
            if n == 0:
                return -1
            if n == 1:
                if nums[0] == target:
                    return 0
                else:
                    return -1
            left = 0
            right = n - 1
            middle = (n - 1) // 2
            while middle != left or middle != right:
                if nums[middle] < nums[right]:
                    right = middle
                elif nums[middle] >= nums[right]:
                    left = middle
                middle = (right + left) // 2
                if right == left + 1:
                    if nums[left] < nums[right]:
                        middle = left
                    else:
                        middle = right
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[middle] == target:
                return middle
            d0 = middle
            left = d0
            if left == 0:
                right = n-1
                middle = left + (right - left + 1) // 2
            else:
                right = left - 1
                length = left + (n - (left - right + 1) + 1) // 2
                if length > n - 1:
                    middle = length - n - 2
                else:
                    middle = length
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[middle] == target:
                return middle
            while nums[middle] != target and (middle != left or middle != right):
                if nums[middle] < target:
                    left = middle
                elif nums[middle] >= target:
                    right = middle
                if left > right:
                    length =  left + (n - (left - right + 1) + 1) // 2
                    if length > n-1:
                        middle = length - n - 2
                    else:
                        middle = length

                else:
                    middle = left + (right - left + 1) // 2
                if nums[middle] == target:
                    break
                if middle == left or middle == right:
                    return -1

            return middle



nums = [8,1,2,3,4,5,6,7]
target = 6
solution = Solution()
a = solution.search(nums, target)
print(a)
