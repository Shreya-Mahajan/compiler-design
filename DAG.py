# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XwxhszG3PI5kuKQ7cFsyB9kWeBdfguAd
"""

import networkx as nx
from matplotlib import pyplot as plt
graph = nx.DiGraph()
graph.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
if nx.is_directed(graph) :
  print('It is a DAG')
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("g1.png", format="PNG")
plt.clf()