import sys
import os

module_path = '/home/reza/Home/BU/SWAXV/Smith-Waterman-SWAVX'
if module_path not in sys.path:
    sys.path.append(module_path)

from GraphEps import epsilon_tuner

compile_args = 'bubblesort.c main.c -D USE_BUBBLE_SORT'
best_action = epsilon_tuner(numIter=500, output_binary="tuned", numTest=1, compile_args=compile_args, optTarget=0, optPass='', param_tune=False)
print(best_action)