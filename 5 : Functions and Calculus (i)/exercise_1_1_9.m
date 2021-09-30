fun = @(t) 10000*exp(-1.1552e-2*t);
% The function can be plotted using fplot:
limits = [0 2000];
fplot(fun,limits)
xlabel('time (minutes)')
ylabel('N')