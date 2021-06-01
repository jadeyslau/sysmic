syms r;
d=2*pi*r*(0.1 + (r/1000));
int(d,r, 0, 1000) 



% syms r;
% N=2*pi*r*(0.1 + 0.002*r);
% g=int(N,r);
% gg=matlabFunction(g);
% n=gg(500)-gg(0);
% n 