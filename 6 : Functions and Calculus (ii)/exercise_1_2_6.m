syms S Vmax K n;
h = Vmax*(S^n)/((K^n) + (S^n));
dh=diff(h,S) 
dh = (S^(n - 1)*Vmax*n)/(K^n + S^n) - (S^n*S^(n - 1)*Vmax*n)/(K^n + S^n)^2
 
dh = simplify(dh)


syms S Vmax K n;
j = Vmax * (S/(K+S)) ^n;
simplify( diff(j,S) )