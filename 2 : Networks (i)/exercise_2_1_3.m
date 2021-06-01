m = [0 1 0; 0 0 1; 1 1 0];
nodes = {'A' 'B' 'C'};
g = biograph(m,nodes);
% view(g)

g.LayoutType = 'radial';

dolayout(g); view(g);

n=[0 1 0 0; 0 0 1 1; 0 0 0 0; 0 0 0 0];
n_nodes = {'V' 'X' 'Y' 'Z'};
n_g = biograph(n,n_nodes);
view(n_g);
