fun = @(t) 0.4 + 0.02*t; 
limits = [0 20]
fplot(fun,limits) 
xlabel('time (minutes)') 
ylabel('volume')
