# -*- coding: utf-8 -*-

import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
import matplotlib.pyplot as plt
from bokeh.io import output_notebook, show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend


# Network
g = nx.newman_watts_strogatz_graph(100,4,0)
g.add_edge(0,50)

# Plotting the network
nx.draw_circular(g, node_size = 5, node_color = 'red')
plt.show()

# Model selection
model = ep.SIModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.01)
cfg.add_model_parameter("Infected", 88)

model.set_initial_status(cfg)


# Simulation execution
iterations = model.iteration_bunch(700)

trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
p = viz.plot(width=400, height=400)
show(p)