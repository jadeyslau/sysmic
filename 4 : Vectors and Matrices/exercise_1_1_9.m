W_sr = zeros(13,10);
W_sr(1,1) = 1;
W_sr(1,10)= 1;
W_sr(2,2) = 1;
W_sr(3,3) = 1;
W_sr(4,3) = 1;
W_sr(5,4) = 1;
W_sr(6,2) = 1; 
W_sr(6,8) = 1;
W_sr(7,6) = 1;
W_sr(8,6) = 1;
W_sr(9,5) = 1;
W_sr(10,6) = 1;
W_sr(10,9) = 1;
W_sr(11,7) = 1;
W_sr(12,7) = 1;
W_sr(13,5) = 1;

W_rs = zeros(13,10);
W_rs(1,2)=1;
W_rs(2,3)=1;
W_rs(3,[1 10])=1;
W_rs(4,4)=1;
W_rs(5,1)=2;
W_rs(5,10)=1;
W_rs(6,6)=1;
W_rs(7,[2 8])=1;
W_rs(8,[5])=1;
W_rs(9,[6])=1;
W_rs(10,[7])=1;
W_rs(11,[6 9])=1;
W_rs(12,[5 9])=1;
W_rs(13,[1 8 10])=1;

% Reaction matrix (output - input)
A = W_sr - W_rs;

% Stoichiometry matrix
S = A';

P = null(A, 'r')
T = null(S, 'r')
