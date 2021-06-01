syms N0 R
assume(R,'real')
assume(R>0)
R = solve( 2*N0 == N0*(1+R)^15, R) 

eval(R) % 0.0473

k = log(1+R) % 0.0462

t3    = 0:15:120;
nt3   = length(t3);
N3    = zeros(1,nt3);
N3(1) = 250;
for j=2:nt3,
     N3(j) = (1+R)*N3(j-1);
end

plot(t3,N3,'o') 
xlabel('time (minutes)','fontsize',12) 
ylabel('N_j','fontsize',12)
