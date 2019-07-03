import numpy as np

class bamodel:
    """
    Generates a bamodel network object, storing the edges and vertices in arrays.
    Probability of connecting to a particular vertex, and the number of edges
    added per node can be defined.
    """
    def __init__(self, prob, m, N, q):
        """
        __init__ - Initialises the bamodel object
        Inputs:
            prob : Probability mode for connecting to particular vertex
            prob = 1 : Pure Preferential Attachment where probability is
            proportional to k, the degree of the vertex
            prob = 2 : Pure Random Attachment where probability is same for
            all vertices.
            prob = 3 : Mixed Attachment where a probability q occurs for mode 1
            and 1 - q for mode 2.
            m : Number of edges added per vertex (The network is initialised with
            number of vertices = m + 1)
            N : Total number of vertices to be added (to initialise self.adj to save computing time)
            q : Probability of a new edge choosing preferential or random attachment
        
        Data attributes:
            self.adj : list containing all neighbours of each vertex (as a list)
            self.k : list containing the degree (number of neightbours) of each vertex
            self.prob, self.m, self.q are as the inputs prob and m respectively.
            self.current : next vertex number to be added (vertex number used to identify each vertex)
            self.num_edges : total number of edges
        """
        #self.adj = [0]*N
        self.k = [0]*N
        self.edges = []
#        for i in range(N):
#            self.adj[i] = []
        self.prob = prob
        self.m = m
        self.current = m # Start adding from vertex m
        # Initialise graph with m vertices (0, 1, ..., m-1) connected to each other
        # (no information as to distribution of edges)
        for i in range(m):
            for j in range(m):
                if i < j:
                    self.edges.append(j)
                    #self.adj[i].append(j)
                    self.k[i] += 1
                    self.edges.append(i)
                    #self.adj[j].append(i)
                    self.k[j] += 1
        self.num_edges = m*(m - 1)/2
        self.q = q
   
    def add_vertex(self):
        """
        add_vertex - Adds a vertex and m edges according to probability mode chosen
        """
        if self.prob == 1:
            if self.m == 1 and len(self.edges) == 0: # Only one vertex to connect to
                self.edges.append(0)
                self.k[0] += 1
                self.edges.append(self.current)
                self.k[self.current] += 1
            else:
                for j in range(self.m):
                    # Choose vertex to connect to
                    #con_vertex = np.random.choice(self.current, 1, p = parr)[0]
                    con_vertex_index = np.random.randint(len(self.edges))
                    con_vertex = self.edges[con_vertex_index]
                    self.edges.append(con_vertex)
                    #self.adj[self.current].append(con_vertex)
                    self.k[self.current] += 1
                    self.edges.append(self.current)
                    #self.adj[con_vertex].append(self.current)
                    self.k[con_vertex] += 1
            self.current += 1 # update new vertex number
            self.num_edges += self.m # added m edges
                
        elif self.prob == 2:
            for j in range(self.m):
                con_vertex = np.random.randint(self.current)
                self.edges.append(self.current)
                #self.adj[self.current].append(con_vertex)
                self.k[self.current] += 1
                self.edges.append(con_vertex)
                #self.adj[con_vertex].append(self.current)
                self.k[con_vertex] += 1
            self.current += 1 # update new vertex number
            self.num_edges += self.m # added m edges

        else:
            for j in range(self.m):
                # Define a variable p between 0 and 1, if p < q then case 1, else case 2
                p = np.random.random()
                if p < self.q:
                    self.prob = 1 # Preferential attachment
                else:
                    self.prob = 2 # Random attachment
                self.add_vertex()
                self.prob = 3
        