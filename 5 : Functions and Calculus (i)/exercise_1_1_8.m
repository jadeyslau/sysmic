% syms N0 Q
% assume(Q,'real')
% assume(Q>0)
% Q = solve( N0/2 == N0*(1-Q)^720, Q);
% 
% eval(Q) % 0.0473
% 
% k = log(1-Q); % 0.0462


fun = @(t) 1000000*exp(-9.627e-4*t);
% The function can be plotted using fplot:
limits = [0 7200];
fplot(fun,limits)
xlabel('time (minutes)')
ylabel('N')

fun = @(t) 1000000*exp(-2.89e-3*t);
% The function can be plotted using fplot:
limits = [0 7200];
fplot(fun,limits)
xlabel('time (minutes)')
ylabel('N')