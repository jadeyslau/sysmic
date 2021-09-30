v = @(S,K,Vmax,n) Vmax*(S^n)/(K^n + S^n);
v1 = @(S) v(S,0.1,10,3);
v2 = @(S) v(S,2,10,3);
v3 = @(S) v(S,8,10,3);
limits = [0 40];
fplot(v1,limits,'r')
hold on
fplot(v2,limits,'b')
fplot(v3,limits,'g')
axis([0 40 0 10])
ylabel('rate')
xlabel('[S]')
legend('km=0.1','km=2','km=8','Location','SouthEast')