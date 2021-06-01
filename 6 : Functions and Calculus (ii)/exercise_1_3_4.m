% syms N(t) N0 k
% eqn = diff(N,t) == k*N;
% cond = N(0) == N0;
% N=dsolve(eqn, cond)


% dN = @(N,r0,K) r0*N*(1-N/K);
% fun = @(N) dN(N,0.0347,1000);
% limits = [0 1200];
% fplot(fun,limits)
% line( [0,1200], [0,0], 'Color','k' )
% ylabel('dN/dt')
% xlabel('N')

% syms N r0 K
% f = r0*N*(1-N/K);
% df = diff(f,N);
% mdf = matlabFunction(df,'vars',[N,r0,K])
% fun = @(N) mdf(N,0.0347,1000);
% limits = [0 1200];
% fplot(fun,limits)
% line( [0,1200], [0,0], 'Color','k' )
% ylabel('d/N x (dN/dt)')
% xlabel('N')
% 
% solve(df==0,N);


syms N(t) N0 r0 K;
eqn = diff(N,t) == r0*N*(1-N/K);
cond = N(0) == N0;
N=dsolve(eqn, cond);
N = simplify(N)

solve(N==K/2,'t') 