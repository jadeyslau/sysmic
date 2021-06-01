fun = @(t,r0,N0,K) K*N0*exp(r0*t)/(K-N0+N0*exp(r0*t)); 
fun1 = @(t) fun(t,0.02,500,20000)
fun2 = @(t) fun(t,0.02,10000,20000)
fun3 = @(t) fun(t,0.02,80000,20000) 
limits = [0 600];
fplot(fun1,limits,'b')
hold on
fplot(fun2,limits,'r')
hold on
fplot(fun3,limits,'g')
yline(20000, '-.b', 'K');
xlabel('time','fontsize',12)
ylabel('N','fontsize',12)
legend('N_0=500','N_0=10000','N_0=80000','Location','SouthEast')


% N0 = 500, The population increases slowly and picks up speed around 100
% mins reaching capacity at around 400 mins.
% N0 = 10000, The population increases steadily, reaching capacity at
% around 250 mins.
% N0 = 80000, Exponential decay within first 100 mins and plateauing at
% capacity around 250 mins.
% If R0 increases, each curve reaches capacity sooner whilst if it
% decreases, the converse occurs and the growth/decay is much slower
% relatively.