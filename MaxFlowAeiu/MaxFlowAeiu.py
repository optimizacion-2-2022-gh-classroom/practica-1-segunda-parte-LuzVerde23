class MaxFlowAeiu:
    '''
        Finds the paths in order to return the maximum flow in the
        network. This class implements the Ford Fulkerson method.
    '''

    def __init__(self,graph):
        '''
        Initialices parts of the problem.
        Attributes:
            graph: defines the graph from a matrix,
            N (bool): the number of the nodes in the graph,
            source (index): the source node of the graph,
            sink (index): the sink node of the graph.
        '''
        self.graph = graph
        self.N = len(graph)
        self.source=0      
        self.sink= self.N-1
        
    
    
        
        
        