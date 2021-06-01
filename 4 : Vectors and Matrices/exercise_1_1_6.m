% Reaction matrix (output - input)
A = [0 1 0; 1 0 0; 0 1 1; 0 0 0] - [1 0 0; 0 1 0; 0 1 0; 0 0 1];

% Stoichiometry matrix
S = A';
 
p = null(A,'r')
t = null(S,'r')