% % create 10x10 matrix with all elements set to 1
% mm = ones(10);
% % set the diagnonal elements equal to zero
% % this means nodes will be connected to every node
% % except themselves
% for i = 1:10 mm(i,i) = 0;
% end
% 
% h = view(biograph(mm))
% [acc, c] = avgClusteringCoefficient(mm)

% cluster coefficient calculation for the case where none of the neighbours of a single node are connected to each other.
mm = zeros(10);
% Fill in 1s in first row
mm(1,:) = 1;
% Fill in 1s in first column
mm(:,1) = 1;
% Eliminate self-connection of node 1.
mm(1,1) = 0;

h = view(biograph(mm))

% Calculate clustering coefficients
[acc, c] = avgClusteringCoefficient(mm)