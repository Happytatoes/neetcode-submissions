class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # parent of each node 
        # (each node starts as its own parent)
        parents = []
        for i in range(len(edges) + 1):
            parents.append(i)

        # rank of each node 
        # (upper bound on height in a compressed tree)
        rank = [1] * (len(edges) + 1)

        # returns root parent of node n
        def find(n):
            if n != parents[n]: 
                parents[n] = find(parents[n])
            return parents[n]

        # returns true if n1 and n2 are
        # not already connected
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # if they have the same root parent
            # they're connected
            if p1 == p2:
                return False

            # we're making this connection
            # and this changes the parent/child relationship
            # between n1/n2/p1/p2
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True

        # returns the edge where n1 is alr connected to n2 
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]