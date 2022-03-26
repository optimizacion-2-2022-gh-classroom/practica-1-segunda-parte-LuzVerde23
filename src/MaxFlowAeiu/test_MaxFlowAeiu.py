#import pytest
import MaxFlowAeiu
import numpy as np
from ortools.graph import pywrapgraph

def test_max_flow():
    """
    Función para comprobar que el método implementado en la función resuleve el problema de flujo máximo de forma adecuada. El resultado
    se compara con un problema que se resuelve con la librería OR-Tools.
    """
    # Solución de un problema de flujo máximo de la librería de OR-Tools (https://developers.google.com/optimization/flow/maxflow)
    
    # Instantiate a SimpleMaxFlow solver.
    max_flow = pywrapgraph.SimpleMaxFlow()
    # Define three parallel arrays: start_nodes, end_nodes, and the capacities
    # between each pair. For instance, the arc from node 0 to node 1 has a
    # capacity of 20.
    start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
    end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
    capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]
    # Add each arc.
    for arc in zip(start_nodes, end_nodes, capacities):
            max_flow.AddArcWithCapacity(arc[0], arc[1], arc[2])
    # Find the maximum flow between node 0 and node 4.
    status = max_flow.Solve(0, 4)
    sol_ORT = max_flow.OptimalFlow()

    # Planteamiento de la red para solucionar el problema con la librería MaxFlowAeiou
    
    mat_inc = [[0,20,30,10,0],[0,0,40,0,30],[0,0,0,10,20],[0,0,5,0,20],[0,0,0,0,0]]
    MF=MaxFlowAeiu(mat_inc)
    sol_MFA = MF.ford_fulkerson()

    assert abs(sol_ORT - sol_MFA) < 0.0001

