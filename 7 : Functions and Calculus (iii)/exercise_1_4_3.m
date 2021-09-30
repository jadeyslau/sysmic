syms t a b X0
mX = matlabFunction(X,'vars',[t a b X0]);
f1 = @(t) mX(t, 10, 1, 1); 
f2 = @(t) mX(t, 50, 5, 1);
f3 = @(t) mX(t, 5, 1, 1);
f4 = @(t) mX(t, 1.2, 0.1, 1); 
limits = [0 10];
hold on
fplot(f1, limits,'k');
fplot(f2, limits,'r');
fplot(f3, limits,'b');
fplot(f4, limits,'g');
axis([0 10 0 11])
ylabel('X')
xlabel('time')
legend('a=10,b=1','a=50,b=5','a=5,b=1','a=0.12,b=0.01','Location','SouthEast')