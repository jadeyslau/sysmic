% Set warnings to hidden
%  warning ('off','all'); % Import the file
%  mm = sbmlimport('R-HSA-71336.sbml'); % Turn warnings back on
%  warning ('on','all');
  mm

% Extract information about the network matrix
[mm_adj , Headings] = getadjacencymatrix(mm);
% Check the number of nodes
no_nodes = size(mm_adj ,1)
% Check the number of edges
no_edges = sum(sum(mm_adj))

% create a biograph from the adjacency matrix
gr = biograph(mm_adj , Headings)
% style species nodes
set(gr.Nodes(1:42),'Shape','ellipse');
set(gr.Nodes(1:42),'Color',[0.2,0.8,0.1]);
% style reaction nodes
set(gr.Nodes(43:end),'Color',[0.5,0.8,1]) % view the network
% view(gr)

% loop over through nodes names
for i=1:length(Headings)
    species = 'G6P';
    location = 'cytosol';
% % display names containing both species AND location
    if contains(Headings(i), species) && contains(Headings(i), location)
        disp([num2str(i) Headings(i)]);
% %         if Headings(i) == 'G6P (cytosol)'
% %             disp([num2str(i) Headings(i)]);
% %         end
    end
end
% 
% % loop over through nodes in matrix
for i=1:length(mm_adj)
 % display edges starting from node 51
     if mm_adj(32,i) == 1
     disp([num2str(i) Headings(i)]);
    end
end
imagesc(mm_adj)