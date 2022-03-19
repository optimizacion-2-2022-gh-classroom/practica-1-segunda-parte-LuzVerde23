from collections import defaultdict

class MaxFlowAeiu:
    '''
        Finds the paths in order to return the maximum flow in the
        network. This class implements the Ford Fulkerson method.
    '''

    def __init__(self,graph):
        '''
        Initialices parts of the problem.
        Attributes:
            graph(matrix): defines the graph from a matrix,
            N (bool): the number of the nodes in the graph,
            source (int): the source node of the graph,
            sink (int): the sink node of the graph.
            residualgraph(matrix):graph where the residual values 
                                  of the edges are updated after 
                                  each iteration.
        '''
        self.graph = graph
        self.N = len(graph)
        self.source=0      
        self.sink= self.N-1
        self.residualgraph = self.graph
    
    def breadth_first_search(self,source,sink,parent): 
        '''
        Defines queue of the visited nodes and the parents of them, and
        so long as the queue of the nodes that need to be visited is not empty, the algorithm goes on.
         Args:
            source (int): the source node of the graph.
            sink (int): the sink node of the graph.
            parent(list): vector for keeping track of the parents of visited nodes.
        Attributes:
            visit(list): vector for keeping track of visited nodes,
            queue(list): the queue of the nodes needed to be visited,
            parent(list): vector for keeping track of the parents of visited nodes.
        Returns:
            (bool): A True/False indicating the presence or absence of a path. 
            It also updates the parent list with the information necessary to reconstruct the path.
  
        '''
        # se inicia el vector de visit en False de acuerdo al nuemero de nodos 
        visit=[False]*(self.N)
        # se inicia el vector queue vacio     
        queue=[]    

        # se agerga al vector queue el valor  de source y 
        # mediante source se asigna al primer espacio del vector visit en true 
        #para comenzar nuestra busqueda del path
        queue.append(source)              
        visit[source]=True               

        while queue:

            # se extrae siempre el primer valor del queue y seb asigna a u
            u = queue.pop(0)
            
            # Se requiere tanto el index como el valor del nodo que sera padre
            for index, value in enumerate(self.graph[u]): 
                if visit[index]== False and value > 0:
                    queue.append(index)
                    visit[index] = True
                    parent[index]=u
        
        # Se crea un check ternario para regresar True 
        # si el camino sido recorrido completamente False de lo contrario
        return True if visit[sink] else False
        
    
    
        
        
        