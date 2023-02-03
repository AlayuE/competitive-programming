class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for i,a in enumerate(temperatures):
            while stack and stack[-1][0] < a:
                item = stack.pop()
                output[item[1]] = i - item[1]
            stack.append([a,i])
        return output