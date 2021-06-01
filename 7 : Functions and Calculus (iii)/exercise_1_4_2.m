syms a b X(t) X0;
eqn = diff(X)==a - b*X;
cond = X(0) == X0;
X = dsolve(eqn,cond);
pretty(X);

dxdt= diff(X)
solx = solve(dxdt, X0)