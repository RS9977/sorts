import sys
import os

module_path = '/home/reza/Home/BU/SWAXV/Smith-Waterman-SWAVX'
if module_path not in sys.path:
    sys.path.append(module_path)

from fully_connected_graph import FullyConnectedGraph
from GraphEps import compile_and_evaluate
import pickle

compile_args = 'bubblesort.c main.c -D USE_BUBBLE_SORT'

with open('graph.pkl', 'rb+') as file:
    graph = pickle.load(file)


num = len(graph.nodes)
ks = [k for k in range(1, num*4, 10)]

with open('resutls.txt', 'w+') as file:
    file.write('Tuning results of the graph:\n')

for k in ks:
    cutoff  = graph.get_kth_biggest_edge_value(k)
    graphss = graph.generate_graph_with_cutoff(cutoff)
    i = 0
    max_node = 0
    i_max = 0
    for graphh in graphss:
        if len(graphh.nodes)>max_node:
            max_node = len(graphh.nodes)
            i_max = i
        i += 1
    val = compile_and_evaluate({}, output_binary="tuned", numTest=1, compile_args=compile_args+ ' ' + ' '.join(graphss[i_max].nodes), optTarget=0, optPass='-O1')
    with open('resutls.txt', 'a+') as file:
        file.write(f"For {k} ->\t{val}\t| Max flags: {max_node}\t| {' '.join(graphss[i_max].nodes)}\n")    