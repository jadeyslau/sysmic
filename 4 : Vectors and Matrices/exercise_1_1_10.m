% s = [A; B; C; D];
% r = [R1; R2; R3; R4];
m = [1; 0; 0; 0];
W_sr = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]
W_rs = [0 1 0 0; 0 0 1 0; 0 0 0 1; 1 0 0 0]
% Reaction matrix (output - input)
A = W_sr - W_rs;

% Stoichiometry matrix
S = A';

P = null(A, 'r')
T = null(S, 'r')




% Q2
% s_2 = [A; B; C];
% r_2 = [R1; R2];
m_2 = [1; 0; 0];
W_sr_2 = [1 1 0; 0 0 0];
W_rs_2 = [0 1 1; 0 0 0];

% Reaction matrix (output - input)
A_2 = W_sr_2 - W_rs_2;

% Stoichiometry matrix
S_2 = A_2';

P_2 = null(A_2, 'r')
T_2 = null(S_2, 'r')