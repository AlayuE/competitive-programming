class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float('inf')
        maxSalary,totalSum = 0,0
        length = len(salary)
        for item in salary:
            if item < minSalary:
                minSalary = item
            if item > maxSalary:
                maxSalary = item
            totalSum += item
        return (totalSum - minSalary - maxSalary) / (length-2)

        