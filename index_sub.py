class Solution:
    def subarraySum(self, arr, target):
        # code here
        n = len(arr)

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]

                if total == target:
                    return [i + 1, j + 1]  

        return [-1]