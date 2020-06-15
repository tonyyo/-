class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        people = sorted(people, key=lambda x : (-x[0], x[1]))
        N = len(people)
        res = []
        for i in range(N):
            res.insert(people[i][1], people[i])  # insert 某个位置时 res可以为空
        return res
if __name__ == '__main__':
    solution = Solution()
    print(solution.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
