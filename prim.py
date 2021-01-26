import heapq
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.adjList = {}
        self.marked = []
        self.pq = []
        self.mst = deque()
        heapq.heapify(self.pq)
        for v in vertices:
            self.addNode(v[0])
            self.addNode(v[1])
            self.addEdge(v[0], v)
            self.addEdge(v[1], v)
        
    def addNode(self, n):
        if n not in self.adjList:
            self.adjList[n] = []

    def addEdge(self, n, e):
        self.adjList[n].append(e)

    def visit(self, ver):
        self.marked.append(ver)
        for vertice in self.adjList[ver]:
            u,v,w = vertice
            if u not in self.marked or v not in self.marked:
                heapq.heappush(self.pq, [w,u,v])

    def prim(self):
        #assuming that 0 in mst
        self.visit(0)
        while(self.pq):
            w,u,v = heapq.heappop(self.pq)
            if u in self.marked and v in self.marked:
                continue
            self.mst.append([u,v,w])
            if u not in self.marked:
                self.visit(u)
            if v not in self.marked:
                self.visit(v)
