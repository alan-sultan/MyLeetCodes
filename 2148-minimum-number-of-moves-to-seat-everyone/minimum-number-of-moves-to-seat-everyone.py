class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        heapify(seats)
        heapify(students)
        ans = 0
        while seats:
            ans += abs(heappop(seats) - heappop(students))
        return ans
        # seats.sort()
        # students.sort()
        # return sum(abs(seats[i] - students[i]) for i in range(len(seats)))