# Disease Spread Simulation on a Simple Lattice Network
Python code for disease spread simluation.

In order to set up the network, I have used Python programming language and
NetworkX library. I have used Newman Watts Strogatz Graph from NetworkX
library to set up ring lattice (I choosed rewiring coefficient as 0 to make it a
ring lattice) and added an extra edge between vertices 0 and M, M being N/2,
N being number of vertices.
Different types of Network can be used from the NetworkX library easily By changing
rewiring coefficient, the lattice becomes a small world network. It can be used for
more realistic simulation.

After that for the simulation model I used Ndlib library. This library has epidemic
models that can be used with created networks. I have used SI model
with the lattice I have created before. It is possible to choose
different beta value and infected nodes when initializing the model. I have
choosed beta value as 0.01. SIR and other epidemic models can also be used easily.
