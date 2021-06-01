syms N(t) N0 r0 K t;
eqn = diff(N,t) == r0*N*(1-N/K);
cond = N(0) == N0;
N=dsolve(eqn, cond);
N=simplify(N)
mN = matlabFunction(N,'vars',[N0,K,r0,t]);

funN100 = @(t) mN(100,1000,0.0347,t);
funN5000 = @(t) mN(5000,1000,0.0347,t);

limits = [0 1200];
fplot(funN100, limits)
hold
fplot(funN5000, limits)