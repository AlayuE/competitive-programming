class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0,len(people)-1
        output = 0
        while left <= right:
            remain = limit - people[right]
            right -= 1
            output += 1
            if left <= right and remain >= people[left]:
                left += 1
        return output
        