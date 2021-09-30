load AdjacencyMatrix.mat
load NodeNames.mat

in_degree  = sum(A);
out_degree = sum(A,2);
% 
% figure(1);
% histogram(in_degree);
% 
% figure(2);
% histogram(out_degree);

avg_in_deg = mean(in_degree);
avg_out_deg = mean(out_degree);

Asub = A(1:200,1:200);
% Plot using biograph
bg = view(biograph(Asub, nodes(1:200),'LayoutType', 'radial'))
% Some node parameters
set(bg.Nodes,'Shape','ellipse')
set(bg.Nodes,'FontSize',10)
set(bg.Nodes,'Size',[50,20])