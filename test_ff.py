import pandas as pd
import networkx as nx
from networkx.algorithms.flow import maximum_flow
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
from src.MaxFlowAeiu.MaxFlowAeiu import MaxFlowAeiu
import numpy as np

d = pd.read_csv('BD/d.csv',header=None)

#Resolvemos usando networkx
# Generamos el arreglo final de tipo "numpy array"
arreglo = d.to_numpy()
G = nx.from_numpy_matrix(arreglo, create_using=nx.DiGraph())
flow_value_nx, flow_dict = nx.maximum_flow(G, 0, 43, capacity='weight')

#Resolvemos usando scipy
arreglo2 = d.to_numpy()
arreglo2=arreglo.astype(int)
graph = csr_matrix(arreglo2)
flow_value_sp=maximum_flow(graph, 0, 43).flow_value

#Resolvemos usando nuestro paquete MaxFlowAeiu
arreglo3 = d.to_numpy()
MF = MaxFlowAeiu(arreglo3)
flow_value_aeiu=MF.ford_fulkerson()

# ejemplo de peq escala

p1=[[0,188,240,160,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,170,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,210,180,0,0,0,0,0],
                    [0,0,0,0,0,140,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,130,90,0,0],
                    [0,0,0,0,0,0,0,0,130,0,0,0,0],
                    [0,0,0,0,0,0,0,0,150,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,160,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,210],
                    [0,0,0,0,0,0,0,0,0,0,0,0,110],
                    [0,0,0,0,0,0,0,0,0,0,0,0,80],
                    [0,0,0,0,0,0,0,0,0,0,0,0,170],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0]]

prueba = np.array(p1)

# networkx
G_p1 = nx.from_numpy_matrix(prueba, create_using=nx.DiGraph())
fv_p1, flow_dict_p1 = nx.maximum_flow(G_p1, 0, 12, capacity='weight')

# scipy
G_p2 = csr_matrix(prueba)
fv_p2=maximum_flow(G_p2, 0, 12).flow_value

# aeiu
MF_p3 = MaxFlowAeiu(prueba)
fv_p3=MF_p3.ford_fulkerson()

def test_vals_1():
    assert(flow_value_nx == flow_value_aeiu)

def test_vals_2():
    assert(flow_value_sp == flow_value_aeiu)

def test_vals_3():
    assert(fv_p1 == fv_p3)

def test_vals_4():
    assert(fv_p2 == fv_p3)
