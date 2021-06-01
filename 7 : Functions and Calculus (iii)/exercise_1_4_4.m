syms X(t) Y(t) a b c g X0 Y0;
eqn = [ diff(X,t) == g*Y - b*X, diff(Y,t) == -c*Y ]
cond = [  X(0) == 0.1, Y(0) == 10 ]
r=dsolve(eqn,cond)
X=simplify(r.X);
Y=simplify(r.Y);
X  
Y 


mX = matlabFunction(X,'vars',[t b X0 Y0 c g])
fX = @(t) mX(t, 1, 0.1, 10, 0.1, 1);
% f2 = @(t) mX(t, 1, 0, 1, 1);
% f3 = @(t) mX(t, 1, 0, 10, 1);
limits = [0 100];
hold on
fplot(fX, limits,'k');
axis([0 10 0 15])
ylabel('X')
xlabel('time')
% legend('c=0.1','c=1','c=10','Location','East')

figure()
mY = matlabFunction(Y,'vars',[t b X0 Y0 c g])
fY = @(t) mY(t, 1, 0.1, 10, 0.1, 1);
limits = [0 100];
hold on
fplot(fY, limits,'k');
axis([0 10 0 15])
ylabel('Y')
xlabel('time')