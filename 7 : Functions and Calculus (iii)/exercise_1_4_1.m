v_rep = @(Y,K,k,n) k*K^n/(K^n + Y^n);
v_act = @(Y,K,k,n) k*K^-n/(K^-n + Y^-n);
ns = [1 3 5 10 100]; 
cols = ['r' 'b' 'g' 'k' 'c']
styl = ['r--' 'b--' 'g--' 'k--' 'c--']
limits = [0 5];
% hold on
% for i=1:5,
%     vt_rep = @(Y) v_rep(Y,1,10,ns(i));
%     fplot(vt_rep,limits,cols(i));
%     
%     vt_act = @(Y) v_act(Y,1,10,ns(i));
%     fplot(vt_act,limits,styl(i));
% end
% axis([0 5 0 10])
% ylabel('dX/dt')
% xlabel('Y')
% legend('n=1','n=3','n=5','n=10','n=100','Location','NorthEast')
% legend('n=-1','n=-3','n=-5','n=-10','n=-100','Location','NorthEast')

% ii

figure()
vt_rep = @(Y) v_rep(Y,1,10,2);
fplot(vt_rep,limits,'g');
hold on
vt_act = @(Y) v_act(Y,1,10,2);
fplot(vt_act,limits,'b');

axis([0 5 0 10])
ylabel('dX/dt')
xlabel('Y')
legend('Repressor','Activator','Location','NorthEast')