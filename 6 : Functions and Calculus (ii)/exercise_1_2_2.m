% v = @(S) 10*S/(1+S);
% limits = [0 10];
% fplot(v,limits)
% axis([0 10 0 10])
% ylabel('rate')
% xlabel('[S]')


% ---


% v = @(S,K,Vmax) Vmax*S/(K + S); 
% v1 = @(S) v(S,0.1,10);
% v2 = @(S) v(S,1,10);
% v3 = @(S) v(S,10,10); 
% limits = [0 10];
% fplot(v1,limits,'r')
% hold on
% fplot(v2,limits,'b')
% fplot(v3,limits,'g')
% axis([0 10 0 10])
% ylabel('rate')
% xlabel('[S]')
% legend('K=0.1','K=1','K=10','Location','SouthEast')

v_max = @(k2,E0) k2*E0;

K = @(kneg1,k2,k1) (kneg1 + k2)/k1;

v = @(S,K,v_max) v_max*S/(K + S);

k_1  = 0.010;
k_neg1 = 0.003;
k_2  = 0.030;
k_2_d  = k_2*2;

E_0 = 4;


K_ = K(k_neg1,k_2,k_1)

v_max1 = v_max(k_2,E_0)

K_d = K(k_neg1,k_2_d,k_1)
v_max_d = v_max(k_2_d,E_0)

v1 = @(S) v(S,K_, v_max1);
v2 = @(S) v(S,K_d, v_max_d);

limits = [0 100];

fplot(v1, limits, 'r')
hold on;
fplot(v2, limits, 'g')

ylabel('rate')
xlabel('[S]')
legend('k_2=0.003','k_2=0.006','Location','SouthEast')
