q = [0 1 0 0 0;
     0 0 1 0 0;
     0 0 0 1 1;
     1 1 1 0 0;
     0 1 0 0 0;
     ];
nodes = {'A' 'B' 'C' 'D' 'E'};
g = biograph(q,nodes);
g.LayoutType = 'equilibrium';
dolayout(g);
vg = view(g)


r = [0 1 0 0 0 0 1 0;
     0 0 1 0 0 0 0 0;
     0 0 0 1 1 0 1 1;
     1 1 1 0 0 0 1 0;
     0 1 0 0 0 0 1 0;
     0 0 0 0 0 0 0 0;
     0 1 0 0 1 0 0 1;
     0 0 0 0 0 1 0 0;
     ];
 
r_nodes = {'A' 'B' 'C' 'D' 'E', 'F' 'G' 'H'};
rg = biograph(r,r_nodes);
rg.LayoutType = 'radial';
dolayout(rg);
rvg = view(rg)