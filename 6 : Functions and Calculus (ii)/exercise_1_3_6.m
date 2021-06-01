% part i
% syms N r0 K
% f = r0*(1-(N/K));
% df = diff(f,N);
% 
% mdf = matlabFunction(df,'vars',[N,r0,K])
% fun = @(N) mdf(N,0.0347,1000);
% limits = [0 1200];
% fplot(fun,limits)
% line( [0,1200], [0,0], 'Color','k' )
% ylabel('d/N x (dN/dt)')
% xlabel('N')

% dN = @(N,r0,K) r0*N*(1-(N/K)^2);
% dN = @(N,r0,K) r0*N*(1-N/K);
dN = @(N,r0,K) r0*N.*(1-((N./K).^2));
fun = @(N) dN(N,0.0347,1000);
limits = [0 1200];
figure()
fplot(fun,limits)
line( [0,1200], [0,0], 'Color','k' )
ylabel('dN/dt')
xlabel('N')

% part ii
% The growth rate increases from N = 0 just before N = 600 reaching a
% maximum of between N = 500 and 600. The function crosses the x-axis when N = 1000, the carry
% capacity. When N < K, the growth rate increases, conversely when N > K the growth
% rate decreases.

% part iii
% The difference between fig 1.3.3 and this plot is that 1.3.3 shows a
% smaller maximum, as well as a more symmetric hyperbole.
% The logistic growth model above dN/dt > 0 appears to increase and 
% decrease at a similar rate whereas the modified model is skewed towards
% a higher population.
% The increase in population of the modified model is more gradual
% relative to the decrease that occurs after the maximum point.

% part iv
% find the maximum of the gradient function with respect to N
syms N r0 K
f = r0*N.*(1-((N./K).^2));

df = diff(f,N);
mdf = matlabFunction(df,'vars',[N,r0,K])
fun = @(N) mdf(N,0.0347,1000);
limits = [0 1200];
figure()
fplot(fun,limits)
line( [0,1200], [0,0], 'Color','k' )
ylabel('d/N x (dN/dt)')
xlabel('N')

solve(df==0,N);

% -(3^(1/2)*K)/3
%  (3^(1/2)*K)/3

% part v

syms N(t) N0 r0 K;
eqn = diff(N,t) == r0*N.*(1-((N./K).^2));
cond = N(0) == N0;
N = dsolve(eqn, cond);
N = simplify(N)

% N = ((K^2*N0^2*exp(2*r0*t))/(K^2 - N0^2 + N0^2*exp(2*r0*t)))^(1/2)

solve(N==0,t);

% 

% part vi

% Logistic growth
syms N(t) N0 r0 K t;
eqn_L = diff(N,t) == r0*N*(1-N/K);
cond = N(0) == N0;
N_L=dsolve(eqn_L, cond);
N_L=simplify(N_L)
mN_L = matlabFunction(N_L,'vars',[N0,K,r0,t]);

funN100_L = @(t) mN_L(100,1000,0.0347,t);
funN5000_L = @(t) mN_L(5000,1000,0.0347,t);

% Modified growth
syms N(t) N0 r0 K t;
eqn_M = diff(N,t) == r0*N.*(1-((N./K).^2));
cond = N(0) == N0;
N_M=dsolve(eqn_M, cond);
N_M=simplify(N_M)
mN_M = matlabFunction(N_M,'vars',[N0,K,r0,t]);

funN100_M = @(t) mN_M(100,1000,0.0347,t);
funN5000_M = @(t) mN_M(5000,1000,0.0347,t);

% Plot

figure()
limits = [0 300];
fplot(funN100_L, limits, 'r')
hold on
fplot(funN100_M, limits, 'b')
ylabel('N')
xlabel('t')
legend('Logistic', 'Modified')
title('N = 100')


figure()
fplot(funN5000_L, limits, 'r')
hold on
fplot(funN5000_M, limits, 'b')
ylabel('N')
xlabel('t')
legend('Logistic', 'Modified')
title('N = 5000')

% part vii
% When N = 100, both Logistic and Modified models increase and appear to do so at similar rates in the first 20 minutes
% however the Modified model increases faster relative to Logistic from 20
% minutes onwards. As such the Modified model reaches carrying capacity
% faster by approximately 100 minutes.
% When N= 5000, the population is way beyond carrying capacity and
% decreases exponentially. The Modifed model has a faster rate of decrease
% reaching carrying capacity 50 minutes before the Logistic model.