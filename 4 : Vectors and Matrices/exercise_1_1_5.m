clc;
% Stoichiometry matrix
S = [2, -2; -1, 1];
 
% Vector of initial particle numbers
m = [4; 4];
 
% Possible reaction vectors for a total of two reactions
u1 = [0; 2]; % Two dimerisations
u2 = [1; 1]; % One dimerisation and one monomerisation
u3 = [2; 0]; % Two monomerisations
 
% Output vectors after two reactions (transposed for readability)
m2_1 = (m + S*u1)'
m2_2 = (m + S*u2)'
m2_3 = (m + S*u3)'
