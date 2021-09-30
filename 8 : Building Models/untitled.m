f = @(v) v/(4+1.5*v+0.008*v^2);
%or to find value of maxima using symbolic equation
syms v
f=v/(4+1.5*v+0.008*v^2)
df=diff(f)
solve(df==0)
% gives solution 10*5^(1/2)=sqrt(500)
subs(f,v,500^.5)
fplot(f)
hold on
xline(sqrt(500), '--')
