syms S Vmax K n;
j = Vmax * (S/(K+S))^n;

dj = diff(j,S);

dj = simplify( dj );

mj = matlabFunction(j,'vars',[S,K,Vmax,n]);
mdj = matlabFunction(dj,'vars',[S,K,Vmax,n]);
f1 = @(S) mj(S,1,10,3.0);
f2 = @(S) mdj(S,1,10,3.0);
limits = [0 10];
figure()
subplot(2,1,1)
fplot(f1,limits,'r')
axis([0 10 0 10])
ylabel('j')
xlabel('[S]')
subplot(2,1,2)
fplot(f2,limits,'r')
ylabel('dj/d[S]')
xlabel('[S]')

% part i
% to find stationary points for dh
d2j = diff(dj,S);
Sm = solve(d2j,S,'Real',true);
% Sm = solve(Sm == 0, 'Real', true);


% part ii
jm = Vmax * (Sm/(K+Sm))^n;
jm = simplify(jm,'IgnoreAnalyticConstraints',true);

% part iii
vs=subs(Sm,[K,Vmax,n],[1.0 10.0 3.0])

% use double() function to display the
% numerical value. 

double(vs)  
subs(j,[S K Vmax n],[vs 1.0 10.0 3.0])  
