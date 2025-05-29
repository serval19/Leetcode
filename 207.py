class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap={ i:[] for i in range(0,numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visitset=set()
        def dfs(crs):
            if crs in visitset:
                return False
            if premap[crs]==[]:
                return True
            visitset.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visitset.remove(crs)
            premap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
