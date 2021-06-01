t = 0:15:180; 
nt = length(t); 
N = zeros(1,nt); 
N(1) = 1;
for j=2:nt,
    N(j) = 2*N(j-1); 
end


plot(t,N,'o') 
xlabel('time (minutes)','fontsize',12) 
ylabel('N_j','fontsize',12)

