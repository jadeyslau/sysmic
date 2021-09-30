% Set warnings to hidden
warning ('off','all'); % Import the file
% mm = sbmlimport('R-HSA-70326.sbml'); % Turn warnings back on
% warning ('on','all');
% mm

% Extract information about the network matrix
[mm_adj , Headings] = getadjacencymatrix(mm);
% Check the number of nodes
no_nodes = size(mm_adj ,1)
% Check the number of edges
no_edges = sum(sum(mm_adj))

% create a biograph from the adjacency matrix
gr = biograph(mm_adj , Headings)
% style species nodes
set(gr.Nodes(1:107),'Shape','ellipse');
set(gr.Nodes(1:107),'Color',[0.2,0.8,0.1]);
% style reaction nodes
set(gr.Nodes(108:end),'Color',[0.5,0.8,1]) % view the network
% view(gr)

% loop over through nodes names
for i=1:length(Headings) species = 'Glc';
location = 'cytosol';
% display names containing both species AND location
if contains(Headings(i), species) ... && contains(Headings(i), location)
end
disp([num2str(i) Headings(i)]);
end

% loop over through nodes in matrix
for i=1:length(mm_adj)
% display edges starting from node 51
    if mm_adj(51,i) == 1
    disp([num2str(i) Headings(i)]);
    end
end

imagesc(mm_adj)