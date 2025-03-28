# GraphCreator
Python code using matplotlib allowing to fast create directed and undirected graphs using a keyboard

# Tutorial
First thing we define in our graph are vertices, with our mouse we can choose their place.
After choosing all vertices coordinates, click enter or mouse scroll.
When vertices are added, this tool bases on its current state, there are two states possible, first vertice state and second vertice state.

First vertice state -> with our keyboard we set the number of the first vertice, then we can click 'a' to switch to the second vertice state.

Second vertice state -> with our keyboard we set the number of the second vertice, then we can click 'a' to add our new edge to the graph. After 'a' key is clicked state switches back to the first vertice state.

When the graph is ready, click q key on your keabord, graph creator class returns a list of vertices coordinates and a list of edges between them.

##Keys:
z -> remove recent added edge
n -> swith current vertice to the second one
b -> switch current vertice back to first one
a -> (works only when on second vertice) add an edge between first vertice chosen and second vertice
d -> set directed graph mode on/off
