class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        # preMap = { i:[] for i in range(numCourses)}
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        output = []
        visitedSet, cycleSet = set()

        def dfs(crs):
            if crs in cycleSet:
                return False
            if crs in visitedSet:
                return True

            cycleSet.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            visitedSet.add(crs)
            output.append(crs)
            cycleSet.remove(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True


array = [[1, 2], [2, 3]]
for crs, pre in array:
    print(crs, pre)
