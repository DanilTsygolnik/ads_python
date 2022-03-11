class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False
        self.index = None

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        new_node = Vertex(v)
        i = self.vertex.index(None)
        new_node.index = i
        self.vertex[i] = new_node
        
    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(len(self.m_adjacency[v])):
            if self.IsEdge(v, i):
                self.RemoveEdge(v, i)

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] and self.m_adjacency[v2][v1]:
            return True
        return False
	
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
    
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
