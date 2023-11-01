class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        # premap = { i:[] for i in range(numCourses)}
        premap = {}
        for i in range(numCourses):
            premap[i] = []
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if premap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False
            visitSet.remove(crs)
            premap[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True


array = [[1, 2], [2, 3]]
for crs, pre in array:
    print(crs, pre)
