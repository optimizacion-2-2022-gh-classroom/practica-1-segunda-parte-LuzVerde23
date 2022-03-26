from pytest import approx
import pandas as pd
import networkx as nx
from networkx.algorithms.flow import maximum_flow
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
from src.MaxFlowAeiu.MaxFlowAeiu import MaxFlowAeiu

d = pd.read_csv('BD/d.csv')

#Resolvemos usando networkx
# Generamos el arreglo final de tipo "numpy array"
arreglo = d.to_numpy()
G = nx.from_numpy_matrix(arreglo, create_using=nx.DiGraph())
flow_value_nx, flow_dict = nx.maximum_flow(G, 0, 43, capacity='weight')

#Resolvemos usando scipy
arreglo = d.to_numpy()
arreglo2=arreglo.astype(int)
graph = csr_matrix(arreglo2)
flow_value_sp=maximum_flow(graph, 0, 43).flow_value

#Resolvemos usando nuestro paquete MaxFlowAeiu
arreglo3 = d.to_numpy()
flow_value_aeiu=MaxFlowAeiu.ford_fulkerson(arreglo3)

def test_vals_1():
    assert(flow_value_nx == flow_value_aeiu)

def test_vals_2():
    assert(flow_value_sp == flow_value_aeiu)
