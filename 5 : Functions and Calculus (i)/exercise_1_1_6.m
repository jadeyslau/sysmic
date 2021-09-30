syms N0 R
assume(R,'real')
assume(R>0)
R = solve( 2*N0 == N0*(1+R)^20, R) 
% R = 2^(1/20) - 1  
eval(R) 


t2 = 0:1:120;
nt2 = length(t2);
N2 = zeros(1,nt2);
N2(1) = 100;
for j=2:nt2,
     N2(j) = 1.0353*N2(j-1);
end


plot(t2,N2,'o') 
xlabel('time (minutes)','fontsize',12) 
ylabel('N_j','fontsize',12)


% plot(t2,N2,'o')
hold on 
fun2 = @(t) 100*exp(log(1.0353)*t); 
limits = [0 120];
fplot(fun2,limits,'r')