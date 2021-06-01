% Settings
options = odeset('InitialStep',0.1,'MaxStep',0.1);
t_range= [0 10];
x_ini= [1 0];
Epo = 1; % Epo concentration

% a
% k1= 1;  %     Rate of EpoR phosphorylation
% k2= 1;  %     Rate of EpoR dephosphorylation

% b
% k1= 2;  %     Rate of EpoR phosphorylation
% k2= 1;  %     Rate of EpoR dephosphorylation

% c
% k1= 1;  %     Rate of EpoR phosphorylation
% k2= 2;  %     Rate of EpoR dephosphorylation

% d
k1= 2;  %     Rate of EpoR phosphorylation
k2= 2;  %     Rate of EpoR dephosphorylation

p = [k1 k2 Epo];
% Simulation
[t,x]=ode45(@model_Epo1,t_range,x_ini,options,p);
% Plot time series of all variables
figure(1);
plot(t,x(:,:));
xlabel('Time ');
ylabel('Epo receptor ');
legend('EpoR', 'p-EpoR');