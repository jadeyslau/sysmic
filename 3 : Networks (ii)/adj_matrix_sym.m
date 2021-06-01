function A = adj_matrix_sym(n)
% Creates a symmetric matrix with randomly assigned 
% zeroes and ones and zeros on the diagonal.
% On the average about half of the entries will be ones.

% Randomly assign zeroes and ones to upper triangular part
% of matrix 
A=triu(randi([0,1],n));
% Set diagonal elements equal to zero
A(1:n+1:end) = 0;
% Copy upper triangular part to lower triangular part
% to obtain symmetric matrix
A = A+triu(A,1)';