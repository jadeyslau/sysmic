m = [0 1 0; 0 0 1; 1 1 0];
nodes = {'A' 'B' 'C'};
g = biograph(m,nodes);
g.LayoutType = 'equilibrium';
dolayout(g);
vg = view(g)

vg.nodes(1)
set(vg.nodes,'Shape','Diamond');
set(vg.nodes,'Color',[0 1 1]);