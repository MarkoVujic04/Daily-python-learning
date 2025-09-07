class Solution(object):
    def permute(self, nums):
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                path.append(nums[i])
                used.add(i)
                backtrack(path, used)
                path.pop()
                used.remove(i)

        backtrack([], set())
        return res
